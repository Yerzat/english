from django.db import models

# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=100)


class Cart(models.Model):
    name = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme)
    
class Word(models.Model):
    cart = models.ForeignKey(Cart)
    
    english_word = models.CharField(max_length=200)
    russian_word = models.CharField(max_length=300)
    transcritption = models.CharField(max_length=100)
    href = models.CharField(max_length=200)
    