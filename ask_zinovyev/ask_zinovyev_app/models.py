from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField()
    rating = models.IntegerField()


class Tag(models.Model):
    label = models.CharField(max_length=30)


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_added = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    rating = models.IntegerField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    date_time_added = models.DateTimeField()
    rating = models.IntegerField()