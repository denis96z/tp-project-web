from django import forms

from ask_zinovyev_app.models import Question, Tag


class QuestionForm(forms.ModelForm):
    tags = forms.CharField(label='Теги', max_length=100, required=False)

    def __init__(self, user, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.__user__ = user

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.user = self.__user__
        instance.save()
        for tag in str(self.data['tags']).split(' '):
            instance.tags.add(Tag.objects.get_or_create(label=tag)[0])
        if commit:
            self.save_m2m()
        return instance

    class Meta:
        model = Question
        fields = ['title', 'description']
