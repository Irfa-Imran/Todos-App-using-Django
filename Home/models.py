from django.db import models

# Create your models here.
class Todos(models.Model):
    todo_name = models.CharField(max_length=100)
    todo_description = models.TextField()