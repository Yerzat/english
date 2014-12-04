from django.db import models

# Create your models here.

class Word(models.Model):
    
    russian_word = models.CharField(max_length=300)
    english_word = models.CharField(max_length=300)
    
    number = models.IntegerField()

class Test(models.Model):
    
    stage = models.IntegerField()
    attempt = models.IntegerField()
    
    current_word = models.CharField(max_length=300)

