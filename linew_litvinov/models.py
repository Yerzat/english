from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self, ):
        return self.name


class Cart(models.Model):
    name = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme)
    
class Word(models.Model):
    cart = models.ForeignKey(Cart)
    
    english_word = models.CharField(max_length=200)
    russian_word = models.CharField(max_length=300)
    transcritption = models.CharField(max_length=100)
    href = models.CharField(max_length=200)


class ThemeImages(models.Model):
    theme = models.OneToOneField(Theme)
    image = models.CharField(max_length=300)
   



 




class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    carts = models.ManyToManyField(Cart)

class Train(models.Model):
    user = models.OneToOneField(User)
    current_word = models.ForeignKey(Word, null=True)
    score = models.IntegerField()


class TrainGame(models.Model):
    user = models.OneToOneField(User)
    current_word = models.OneToOneField(Word, null=True)
    score = models.IntegerField()
    cart = models.OneToOneField(Cart)
    stage = models.IntegerField()

class TrainGame1(models.Model):
    user = models.OneToOneField(User)
    current_word = models.OneToOneField(Word, null=True)
    score = models.IntegerField()
    cart = models.OneToOneField(Cart)
    stage = models.IntegerField()