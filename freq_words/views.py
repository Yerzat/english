from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext

import random

from .models import Word, Test



def populate(request):
    
    from bs4 import BeautifulSoup
    import urllib2
    def get_words(url, words):
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)
	tables = soup.find_all('table')
	table = tables[3]
	trs = table.find_all('tr')
	for tr in trs:
		td = tr.find_all('td')
		try:
			words[int(td[0].get_text())] = (td[1].get_text(), td[2].get_text())
			words[int(td[3].get_text())] = (td[4].get_text(), td[5].get_text())
		except:
			pass
	return words

    urls = ["http://en365.ru/top1000.htm",
            "http://en365.ru/top1000a.htm",
            "http://en365.ru/top1000b.htm"]

    words = dict([])

    for url in urls:
        words = get_words(url, words)
    
    for key in words.keys():
        w = Word(russian_word=words[key][0], english_word=words[key][1], number=key)
        w.save()
    
    return HttpResponse("Populated!")


def test(request):
    
    def result():
        context = RequestContext(request)
        context_dict = dict([])
        context_dict['test'] = test
        del request.session['test_id']
        return render_to_response('freq_words/result.html', context_dict, context)
        
    if request.session.get('test_id'):
        print 'session exists'
        test_id = request.session.get('test_id')
        test = Test.objects.get(id = test_id)
    else:
        print 'session created'
        test = Test.objects.create(stage=1, attempt=0)
        request.session['test_id'] = test.id
    
    if request.method == "POST":
        word = request.POST['word']
        if word == test.current_word:
            print "YEAH! You are right!!!"
            test.stage += 1
            test.save()
        else:
            print "NIHRENA!"
            print "|" + word + "|", "|" + test.current_word + "|"
            test.attempt += 1
            test.save()
        if test.attempt > 2:
            context = RequestContext(request)
            context_dict = dict([])
            context_dict['test'] = test
            del request.session['test_id']
            return render_to_response('freq_words/result.html', context_dict, context)
    
    if test.stage >= 10:
        context = RequestContext(request)
        context_dict = dict([])
        context_dict['test'] = test
        del request.session['test_id']
        return render_to_response('freq_words/result.html', context_dict, context)
    
    if test.stage == 1:
        number = random.randint(30, 50)
    elif test.stage == 2:
        number = random.randint(51, 100)
    else:
        number = random.randint((test.stage - 2)*100, (test.stage - 2)*100 + 100)
    
    word = Word.objects.get(number=number)
    test.current_word = word.russian_word
    test.save()
    
    words = []
    
    print test.stage, test.current_word, test.attempt
    
    for i in range(4):
        words.append( Word.objects.get(number=number-i) )
    random.shuffle(words)
    
    context = RequestContext(request)
    context_dict = dict([])
    context_dict['words'] = words
    context_dict['target'] = test.current_word
    return render_to_response('freq_words/test.html', context_dict, context)
