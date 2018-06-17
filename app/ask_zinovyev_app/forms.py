from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from ask_zinovyev_app.models import Question, Tag, Answer


class NewQuestionForm(forms.ModelForm):
    __user = None
    tags = forms.CharField(label='Теги', max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super(NewQuestionForm, self).__init__(*args, **kwargs)

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def save(self, commit=True):
        instance = super(NewQuestionForm, self).save(commit=False)
        instance.user = self.__user
        instance.save()
        for tag in str(self.data['tags']).split(' '):
            if tag == '':
                continue
            instance.tags.add(Tag.objects.get_or_create(label=tag)[0])
        if commit:
            self.save_m2m()
        return instance

    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):
    def __init__(self, user, question, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.__user__ = user
        self.__question__ = question

    def save(self, commit=True):
        instance = super(AnswerForm, self).save(commit=False)
        instance.user = self.__user__
        instance.question = self.__question__
        instance.save()
        return instance

    class Meta:
        model = Answer
        fields = ['description']


class SignUpForm(UserCreationForm):
    __request = None
    email = forms.EmailField(label="Email")

    def get_request(self):
        return self.__request

    def set_request(self, request):
        self.__request = request

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        login(self.__request, user)
        return user
