from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Journal(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    problem = models.TextField(verbose_name='Проблема', default='Заглушка')
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name='Место')
    executor = models.CharField(max_length=100, blank=True, null=True, verbose_name='Исполнитель')

    def __str__(self):
        return self.problem
    
    def get_absolute_url(self):
           return reverse('journal:test')



# Create your models here.
