from django.db import models
from django.contrib.auth.models import User
import random

class Question(models.Model):
    question = models.CharField('Вопрос', max_length=20, unique=True)

    class Meta:
        db_table = 'question'
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'


class QuestionUser(models.Model):

    ANSWER = [
        ('0', 'Да'),
        ('1', 'Нет'),
        ('2', 'Возможно'),
        ('3', 'Вопрос не ясен'),
        ('4', 'Абсолютно точно'),
        ('5', 'Никогда'),
        ('6', 'Даже не думай'),
        ('7', 'Сконцентрируйся и спроси опять')
    ]
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='Вопрос')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    answer = models.CharField('Ответ', default=0, choices=ANSWER, max_length=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'question_user'
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'