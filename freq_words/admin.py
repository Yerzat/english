from django.contrib import admin

from .models import Word

class WordAdmin(admin.ModelAdmin):
    class Meta:
        model = Word

admin.site.register(Word, WordAdmin)