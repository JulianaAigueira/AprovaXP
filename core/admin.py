from django.contrib import admin
from .models import Profile, Subject, Topic, Question, Choice

# Registrando as tabelas para que elas apareçam no painel admin
admin.site.register(Profile)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Choice)