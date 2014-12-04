from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
import datetime

from .models import Word

def home(request):
    context = RequestContext(request)
    return render_to_response('words/home.html', locals(), context)


def train(request):
    context = RequestContext(request)
    words = Word.objects.all()
    return render_to_response('words/train.html', locals(), context)

def boot(request):
    context = RequestContext(request)
    return render_to_response('words/boot.html', locals(), context)
