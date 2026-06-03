from rest_framework import viewsets
from .models import Subject, Topic, Question
from .serializers import SubjectSerializer, TopicSerializer, QuestionSerializer

# Garçom das Matérias
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# Garçom dos Tópicos
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

# Garçom das Questões (e suas alternativas)
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer