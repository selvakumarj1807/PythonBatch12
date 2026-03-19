from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)