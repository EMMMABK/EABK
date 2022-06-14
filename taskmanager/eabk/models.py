from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Information')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Exersise'
        verbose_name_plural = 'Exersises'
