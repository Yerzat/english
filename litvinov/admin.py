from django.contrib import admin

from .models import Word, Cart, Theme

class WordAdmin(admin.ModelAdmin):
    class Meta:
        model = Word

admin.site.register(Word, WordAdmin)

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)

class ThemeAdmin(admin.ModelAdmin):
    class Meta:
        model = Theme

admin.site.register(Theme, ThemeAdmin)