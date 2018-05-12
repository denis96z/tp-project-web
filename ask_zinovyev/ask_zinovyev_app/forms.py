from django import forms

from ask_zinovyev_app.models import Question


class QuestionForm(forms.ModelForm):
    tags = forms.CharField(label='Теги', max_length=100)

    class Meta:
        model = Question
        fields = ['title', 'description']
