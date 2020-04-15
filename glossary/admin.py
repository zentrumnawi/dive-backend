from django.contrib import admin
from .models import GlossaryEntry
from utility.forms import HasImgForm


class GlossaryEntryAdmin(admin.ModelAdmin):
    form = HasImgForm
    list_display = ("id", "term")


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
