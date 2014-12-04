from django.contrib import admin

from .models import Questions, Answers

class QuestionsAdmin(admin.ModelAdmin):
    class Meta:
        model = Questions

admin.site.register(Questions, QuestionsAdmin)


class AnswersAdmin(admin.ModelAdmin):
    class Meta:
        model = Answers

admin.site.register(Answers, AnswersAdmin)
