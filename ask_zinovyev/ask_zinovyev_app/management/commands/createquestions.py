import random
from django.core.management.base import BaseCommand

from ask_zinovyev_app.models import Question, User


class Command(BaseCommand):
    help = 'Adds random data to database'

    def add_arguments(self, parser):
        parser.add_argument('num-questions', nargs=1, type=int)

    def handle(self, *args, **options):
        num_questions = options['num-questions'][0]
        if num_questions <= 0:
            self.stdout.write('Number of questions (num-questions) is expected to be greater than 0.')
            return
        users = User.objects.all()
        for i in range(num_questions):
            question = Question()
            question.title = "Вопрос №" + str(i)
            question.description = "Пояснение к вопросу"
            question.user = random.choice(users)
            question.save()
        self.stdout.write('Successfully created {0} questions.'.format(num_questions))
