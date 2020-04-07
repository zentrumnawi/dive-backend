from django.contrib import admin
from .models import QuizQuestion, QuizAnswer
from utility.forms import HasImgAltForm


class QuizQuestionAdmin(admin.ModelAdmin):
    form = HasImgAltForm
    list_display = ("id", "text")


admin.site.register(QuizQuestion, QuizQuestionAdmin)


class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "text", "correct")


admin.site.register(QuizAnswer, QuizAnswerAdmin)
