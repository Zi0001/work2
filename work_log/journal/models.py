from django.db import models
from django.urls import reverse

class Journal(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    completed_work = models.TextField(verbose_name='Выполненные работы')
    place_of_work = models.CharField(max_length=200, verbose_name='Место выполнения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.completed_work
    
    def get_absolute_url(self):
           return reverse('journal:test')



# Create your models here.
