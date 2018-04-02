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
    rate = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_time_added']


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE)
    value = models.BooleanField(verbose_name='True if like, False if dislike')

    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)
        self.pub.rate += 1 if self.value else -1

    class Meta:
        unique_together = ('user', 'pub')


class Question(Publication):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.question.title