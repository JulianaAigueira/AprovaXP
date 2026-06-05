from rest_framework import serializers
from .models import Profile, Subject, Topic, Question, Choice
from django.contrib.auth.models import User

# 1. Tradutor de Alternativas
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        # Escolhemos quais campos o celular vai receber
        fields = ['id', 'text', 'is_correct']

# 2. Tradutor de Questões (Ele puxa as alternativas junto!)
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'statement', 'image', 'explanation', 'difficulty', 'choices']

# 3. Tradutor de Tópicos
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'order']

# 4. Tradutor de Matérias
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'icon_color']

# 5. Tradutor de Cadastro de Aluno
class RegisterSerializer(serializers.ModelSerializer):
    # O write_only=True garante que a senha nunca seja mostrada ao buscar os dados, só na hora de salvar!
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Cria o usuário com a senha criptografada em segurança
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Já cria o Perfil do jogo (nível 1, 0 XP, 5 vidas) amarrado a esse usuário
        Profile.objects.create(user=user)
        return user

# 6. Tradutor do Ranking (Perfil do Aluno)
class ProfileSerializer(serializers.ModelSerializer):
    # Puxa o nome do usuário que está amarrado a este perfil
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'xp', 'current_lives']