from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, TopicViewSet, QuestionViewSet

# O Roteador automático do Django REST Framework
router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]