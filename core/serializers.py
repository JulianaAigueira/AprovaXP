from rest_framework import serializers
from .models import Profile, Subject, Topic, Question, Choice

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