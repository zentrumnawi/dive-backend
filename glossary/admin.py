from django.contrib import admin
from .models import GlossaryEntry
from utility.forms import HasImgAltForm


class GlossaryEntryAdmin(admin.ModelAdmin):
    form = HasImgAltForm
    list_display = ("id", "term")


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
