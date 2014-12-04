from django.db import models

# Create your models here.

TYPES_OF_WORDS = (
    ('Verbs', 'Verbs'),
    ('Noun', 'Noun'),
    ('Adjective', 'Adjective'),
    ('Adverb', 'Adverb'),
    ('None', 'None'),
)


class Word(models.Model):
    
    russian_word = models.CharField(max_length=300)
    english_word = models.CharField(max_length=300)
    
    type_of_word = models.CharField(max_length=20, choices=TYPES_OF_WORDS)
    
    