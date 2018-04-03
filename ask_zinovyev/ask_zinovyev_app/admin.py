from django.contrib import admin

from ask_zinovyev_app.models import User, Question, Tag, Answer

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
