from django.forms import ModelForm
from django.db import models

from ask_zinovyev_app.models import Question


class NewQuestionForm(ModelForm):
    tags = models.TextField(blank=False, verbose_name='Теги, перечисленные через пробел')

    class Meta:
        model = Question
        fields = ['title', 'description']
