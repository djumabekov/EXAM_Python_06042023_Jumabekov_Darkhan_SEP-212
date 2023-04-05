from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    complete = models.BooleanField(default=False, verbose_name='Завершено')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']