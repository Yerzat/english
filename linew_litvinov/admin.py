from django.contrib import admin

from .models import Word, Cart, Theme, UserProfile, ThemeImages

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

class ThemeImagesAdmin(admin.ModelAdmin):
    class Meta:
        model = ThemeImages

admin.site.register(ThemeImages, ThemeImagesAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)