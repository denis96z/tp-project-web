from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m/%d/')


class Tag(models.Model):
    label = models.CharField(max_length=30, verbose_name=u'Tag title.')

    def __str__(self):
        return self.label


class Publication(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time_added = models.DateTimeField(default=datetime.now)
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_time_added']


class Question(Publication):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.question.title