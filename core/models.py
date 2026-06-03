from django.db import models
from django.contrib.auth.models import User

# 1. PERFIL DO ALUNO (Ligado ao usuário padrão do Django)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    current_lives = models.IntegerField(default=5)
    streak_days = models.IntegerField(default=0)
    last_activity = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username} - Level {self.level}"

# 2. MATÉRIA
class Subject(models.Model):
    name = models.CharField(max_length=100)
    icon_color = models.CharField(max_length=7, help_text="Cor em Hexadecimal, ex: #6c5ce7")

    def __str__(self):
        return self.name

# 3. TÓPICO (A Trilha)
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=150)
    order = models.IntegerField(help_text="1 para o primeiro tópico, 2 para o segundo, etc.")

    def __str__(self):
        return f"{self.subject.name} - {self.title}"

# 4. QUESTÃO (A pergunta padrão ENEM)
class Question(models.Model):
    DIFFICULTY_LEVELS = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    ]

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
    statement = models.TextField()
    image = models.ImageField(upload_to='questions_images/', null=True, blank=True)
    explanation = models.TextField(help_text="Explicação que aparece após o aluno responder")
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_LEVELS, default='M')

    def __str__(self):
        return f"Question: {self.statement[:50]}..."

# 5. ALTERNATIVA
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{'✅' if self.is_correct else '❌'} - {self.text[:30]}"