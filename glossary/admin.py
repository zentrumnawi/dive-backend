from django.contrib import admin
from .models import GlossaryEntry


class GlossaryEntryAdmin(admin.ModelAdmin):
    list_display = ["id", "term"]


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
