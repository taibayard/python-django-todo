from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.text
