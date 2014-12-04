
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Questions, Answers


def grammar(request, index):
    context = RequestContext(request)
    
    
    all_questions = Questions.objects.all()
    
    index = int(index)
    index += 1
    if index > len(all_questions):
        return render_to_response('grammar/result.html', locals(), context)
        
    question = Questions.objects.get(index=index)
    
    answers = Answers.objects.filter(question=question)
    
    print question.question
    
    return render_to_response('grammar/grammar.html', locals(), context)