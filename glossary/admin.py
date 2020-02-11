from django.contrib import admin
from .models import GlossaryEntry

# Register your models here.


class GlossaryEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "term")


admin.site.register(GlossaryEntry, GlossaryEntryAdmin)
