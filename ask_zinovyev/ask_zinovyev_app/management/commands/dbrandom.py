import random
from django.core.management.base import BaseCommand

from ask_zinovyev_app.models import Question, User


class Command(BaseCommand):
    help = 'Adds random data to database'

    def handle(self, *args, **options):
        users = User.objects.all()
        for i in range(10000):
            question = Question()
            question.title = "Вопрос №" + str(i)
            question.description = "Пояснение к вопросу"
            question.user = random.choice(users)
            question.save()