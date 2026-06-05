from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User  # <-- Faltava essa linha!
from .models import Subject, Topic, Question, Choice, Profile
from .serializers import SubjectSerializer, TopicSerializer, QuestionSerializer, RegisterSerializer, ProfileSerializer

# Garçom das Matérias
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

# Garçom dos Tópicos
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

# Garçom das Questões (Agora com inteligência de Gamificação!)
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    # Criando uma rota específica para responder: /api/questions/1/answer/
    @action(detail=True, methods=['post'])
    def answer(self, request, pk=None):
        question = self.get_object() # Pega a questão atual
        choice_id = request.data.get('choice_id') # Pega a resposta que o celular enviou

        if not choice_id:
            return Response({'error': 'Você precisa enviar o choice_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Tenta encontrar a alternativa escolhida dentro dessa questão
            selected_choice = question.choices.get(id=choice_id)
        except Choice.DoesNotExist:
            return Response({'error': 'Alternativa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Busca o Perfil do aluno logado (ou cria um se for o primeiro acesso)
        profile, created = Profile.objects.get_or_create(user=request.user)

        # Lógica de Gamificação
        is_correct = selected_choice.is_correct

        if is_correct:
            profile.xp += 10
            mensagem = "Acertou! +10 XP"
        else:
            profile.current_lives -= 1
            mensagem = "Errou! -1 Vida"

        profile.save() # Salva as novas vidas/XP no banco de dados

        # Devolve o resultado para a tela do celular piscar verde ou vermelho
        return Response({
            'is_correct': is_correct,
            'message': mensagem,
            'current_xp': profile.xp,
            'current_lives': profile.current_lives,
            'explanation': question.explanation # Envia a explicação para o aluno ler

        })

# A Recepção: Rota pública para criar novos alunos
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny] # <- Libera a porta sem precisar de Token!
    serializer_class = RegisterSerializer

# O Pódio: Rota para ver o Top 10 de XP
class LeaderboardView(generics.ListAPIView):
    # Vai no banco, ordena pelo XP decrescente (sinal de menos) e pega os 10 primeiros
    queryset = Profile.objects.all().order_by('-xp')[:10]
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated] # Só quem tem a pulseira VIP pode ver o ranking