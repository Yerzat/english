from django.db import models

# Create your models here.

class Question(models.Model):
    
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)


class Answer(models.Model):
    
    answer = models.CharField(max_length=100)



class Questions(models.Model):
    
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    index = models.IntegerField()
    
    def __unicode__(self, ):
        return self.question

class Answers(models.Model):
    
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Questions)
    
