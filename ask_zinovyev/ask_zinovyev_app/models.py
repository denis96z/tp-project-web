from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m/%d/')


class Tag(models.Model):
    label = models.CharField(unique=True, max_length=15, verbose_name='Название')

    def __str__(self):
        return self.label


class Publication(models.Model):
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_time_added = models.DateTimeField(default=datetime.now, verbose_name='Дата добавления:')
    rate = models.IntegerField(verbose_name='Рейтинг')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_time_added']


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Публикация')
    value = models.BooleanField(verbose_name='Лайк (True), Дизлайк (False)')

    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)
        self.pub.rate += 1 if self.value else -1

    def delete(self, *args, **kwargs):
        super(Rating, self).delete(*args, **kwargs)
        self.pub.rate += -1 if self.value else 1

    class Meta:
        unique_together = ('user', 'pub')


class Question(Publication):
    title = models.CharField(max_length=100, verbose_name='Название')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    num_answers = models.IntegerField(default=0, verbose_name='Количество ответов')

    def __str__(self):
        return self.title


class Answer(Publication):
    quest = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    is_correct = models.BooleanField(verbose_name='Правильный ответ')

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)
        self.quest.num_answers += 1

    def delete(self, *args, **kwargs):
        super(Answer, self).delete(*args, **kwargs)
        self.quest.num_answers -= 1

    def __str__(self):
        return self.quest.title