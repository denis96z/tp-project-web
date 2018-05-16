from django import forms
from django.contrib.auth import authenticate, login

from ask_zinovyev_app.models import Question, Tag, Answer


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
            if tag == "":
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def sign_in(self, request):
        if self.is_valid():
            user = authenticate(request, username=self.cleaned_data['username'],
                                password=self.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return True
            else:
                self.errors[''] = 'Неверный логин или пароль'
        return False
