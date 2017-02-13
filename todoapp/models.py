from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.text
