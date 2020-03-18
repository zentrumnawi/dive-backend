from django.contrib import admin
from .models import QuizQuestion


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text")


admin.site.register(QuizQuestion, QuizQuestionAdmin)
