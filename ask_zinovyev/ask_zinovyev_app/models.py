from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m/%d/')


class Tag(models.Model):
    label = models.CharField(unique=True, max_length=15, verbose_name='Название')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_time_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', editable=False)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг', editable=False)
    num_answers = models.PositiveIntegerField(default=0, verbose_name='Количество ответов', editable=False)
    is_active = models.BooleanField(default=True, verbose_name='Отображается на сайте')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-date_time_added', '-rating']


class QuestionRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    is_like = models.BooleanField(default=True, verbose_name='Понравилось')
    date_time_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def save(self, *args, **kwargs):
        super(QuestionRating, self).save(*args, **kwargs)
        self.question.rating += 1 if self.is_like else -1

    def delete(self, *args, **kwargs):
        super(QuestionRating, self).delete(*args, **kwargs)
        self.question.rating += 1 if self.is_like else -1

    class Meta:
        verbose_name = 'Рейтинг вопроса'
        verbose_name_plural = 'Рейтинги вопросов'
        unique_together = ('user', 'question')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    description = models.TextField(blank=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_time_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', editable=False)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг', editable=False)
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ', editable=False)
    is_active = models.BooleanField(default=True, verbose_name='Отображается на сайте')

    def save(self, *args, **kwargs):
        super(Answer, self).save(*args, **kwargs)
        if not self.pk:
            self.question.num_answers += 1

    def delete(self, *args, **kwargs):
        super(Answer, self).delete(*args, **kwargs)
        self.question.num_answers -= 1

    def __str__(self):
        return self.question.title + '(' + str(self.pk) + ')'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-date_time_added', '-rating']


class AnswerRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Ответ')
    is_like = models.BooleanField(default=True, verbose_name='Понравилось')
    date_time_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def save(self, *args, **kwargs):
        super(AnswerRating, self).save(*args, **kwargs)
        self.answer.rating += 1 if self.is_like else -1

    def delete(self, *args, **kwargs):
        super(AnswerRating, self).delete(*args, **kwargs)
        self.answer.rating += 1 if self.is_like else -1

    class Meta:
        verbose_name = 'Рейтинг ответа'
        verbose_name_plural = 'Рейтинги ответов'
        unique_together = ('user', 'answer')