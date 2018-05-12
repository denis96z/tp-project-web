from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import Http404


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/')


class Tag(models.Model):
    label = models.CharField(unique=True, max_length=15, verbose_name='Название')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class PublicationManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(is_active=True)

    def popular(self):
        return self.active().order_by('-rating')

    def recent(self):
        return self.active().order_by('-date_time_added')


class Publication(models.Model):
    description = models.TextField(blank=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    date_time_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', editable=False)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг', editable=False)
    is_active = models.BooleanField(default=True, verbose_name='Отображается на сайте')

    class Meta:
        abstract = True
        ordering = ['-date_time_added', '-rating']


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Публикация')
    is_like = models.BooleanField(default=True, verbose_name='Понравилось')
    date_time_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def save(self, *args, **kwargs):
        super(Rating, self).save(*args, **kwargs)
        self.publication.rating += 1 if self.is_like else -1
        self.publication.save()

    def delete(self, *args, **kwargs):
        self.publication.rating += 1 if self.is_like else -1
        self.publication.save()
        super(Rating, self).delete(*args, **kwargs)

    class Meta:
        abstract = True
        unique_together = ('user', 'publication')


class QuestionManager(PublicationManager):
    def by_tag(self, tag_id):
        return self.active().filter(tags__pk=tag_id).order_by('-date_time_added')


class Question(Publication):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    num_answers = models.PositiveIntegerField(default=0, verbose_name='Количество ответов', editable=False)

    objects = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class QuestionRating(Rating):
    publication = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')

    class Meta:
        verbose_name = 'Рейтинг вопроса'
        verbose_name_plural = 'Рейтинги вопросов'


class AnswerManager(PublicationManager):
    def by_question(self, question_id):
        return self.active().filter(question__pk=question_id).order_by('-date_time_added')


class Answer(Publication):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ', editable=False)

    objects = AnswerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.question.num_answers += 1
            self.question.save()
        super(Answer, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.question.num_answers -= 1
        self.question.save()
        super(Answer, self).delete(*args, **kwargs)

    def __str__(self):
        return self.question.title + ':' + str(self.pk) + ')'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class AnswerRating(Rating):
    publication = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Рейтинг ответа'
        verbose_name_plural = 'Рейтинги ответов'


def get_active_or_404(model, **kwargs):
    try:
        return model.objects.active().get(**kwargs)
    except model.DoesNotExist:
        raise Http404
