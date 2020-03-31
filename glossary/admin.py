from django.contrib import admin
from .models import GlossaryEntry
from django import forms


class GlossaryEntryAdmin(admin.ModelAdmin):
    form = HasImgAltForm
    list_display = ("id", "term")


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
