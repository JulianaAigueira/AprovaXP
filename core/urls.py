from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, TopicViewSet, QuestionViewSet, RegisterView, LeaderboardView

# O Roteador automático do Django REST Framework
router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'), # <-- A porta de cadastro!
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]