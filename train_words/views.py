
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

import random

from linew_litvinov.models import Cart, Word

def test(request):
    context = RequestContext(request)
    
    return render_to_response('train_words/train.html', locals(), context)

def train(request, card_id, i):
    context = RequestContext(request)
    
    cart = Cart.objects.get(id=card_id)
    words = cart.word_set.all()
    
    i = int(i)
    word = words[i]
    i += 1
    
    try: transcription = word.transcritption
    except: transcription = None
    if not (transcription and "?" not in transcription):
        del transcription
    
    guess_words = []
    guess_words.append(word)
    
    for k in range(3):
        guess_word = random.choice(words)
        while guess_word == word or guess_word in guess_words:
            guess_word = random.choice(words)
        guess_words.append(guess_word)
    
    random.shuffle(guess_words)
    
    return render_to_response('train_words/train.html', locals(), context)
    