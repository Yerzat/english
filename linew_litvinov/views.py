# encoding=utf8
from bs4 import BeautifulSoup
import urllib2

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Cart, Theme, Word, UserProfile, Train, TrainGame1, ThemeImages

def get_all_words(html):
	soup = BeautifulSoup(html)
	tables = soup.find_all('table', 'list songs bordered v-middle')
	words = create_words(tables)
	names = get_names(html)
	all_words = dict([])
	i = 0
	for name in names:
		all_words[name] = words[i]
		i += 1
	return all_words

def full_words(trs):
	words = []
	for tr in trs:
		w = dict([])
		tds = tr.find_all('td')
		a = tds[0].find_all('a')
		if a:
			try:
				s = a[0].get('href')
				s = s.split("'")
				word['href'] = s[1]
			except:
				pass
		w['word'] = tds[1].get_text()
		words.append(w)
	return words

def create_words(tables):
	table_words = []
	for table in tables:
		trs = table.find_all('tr')
		words = full_words(trs)
		table_words.append(words)
	return table_words

def get_names(html):
	def names(h2):
		h = []
		for hh in h2:
			if not hh.find_all('a'):
				h.append(hh.get_text())
		return h
	soup = BeautifulSoup(html)
	h = soup.find_all("div", "cats-list")
	h2 = h[0].find_all('h2')
	return names(h2)

def get_table_words(url):
	html = urllib2.urlopen(url).read()
	return get_all_words(html)

def print_words(table_words):
	for k in table_words:
		print "_____________________________________________"
		print k
		print "_____________________________________________"
		for word in table_words[k]:
			print word['word']

def get_a(html):
	soup = BeautifulSoup(html)
	tables = soup.find_all('table', 'list')
	trs = tables[0].find_all('tr')
	a = []
	for tr in trs:
		td = tr.find_all('td')[1]
		a.append(td.a)
	return a

def get_vocabulary(url):
	html_main = urllib2.urlopen(url).read()
	a = get_a(html_main)
	vocabulary = dict([])
	u = "http://iloveenglish.ru"
	for aa in a:
		try:
			table_words = get_table_words(u + aa.get('href'))
			vocabulary[aa.get_text()] = table_words
		except:
			pass
	return vocabulary

def print_vocabulary(vocabulary):
	for k in vocabulary.keys():
		print
		print k
		print
		for table_words in vocabulary[k]:
			try:
				print_words(table_words)
			except: pass
		print "##################################################"
		print "##################################################"
		print
		print


from .models import Cart, Theme, Word

from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext



def populate(request):
    url = "http://iloveenglish.ru/vocabulary"
    vocabulary = get_vocabulary(url)

    for key in vocabulary.keys():
        theme = Theme(name=key)
        theme.save()
        tv = vocabulary[key]
        for k in tv:
            cart = Cart(name=k, theme=theme)
            cart.save()
            for word in tv[k]:
    		s = word["word"].strip()
                if '[' in s:
                    s = s.split(u" — ")
                    english_word = s[0]
                    d = s[1].split('[')
                    russian_word = d[0]
                    transcription = d[1][:len(d[1]) - 1]
                    try:
                        href = word["href"]
                        word = Word(russian_word=russian_word,
                                english_word=english_word,
                                cart=cart,
                                href=href, transcritption=transcription)
                    except:
                        word = Word(russian_word=russian_word,
                                english_word=english_word,
                                cart=cart, transcritption=transcription)

                else:
                    s = s.split(u" — ")
                    english_word = s[0]
                    russian_word = s[1]
                    try:
                        href = word["href"]
                        word = Word(russian_word=russian_word,
                                english_word=english_word,
                                cart=cart,
                                href=href)
                    except:
                        word = Word(russian_word=russian_word,
                                english_word=english_word,
                                cart=cart)
                word.save()
    
    return HttpResponse("Populated!")


def words(request):
    context = RequestContext(request)
    
    themes = Theme.objects.all()
    carts = Cart.objects.all()
    
    context_dict = dict([])
    
    
    return render_to_response('linew_litvinov/words.html', locals(), context)

def card(request, card_id):
    context = RequestContext(request)
    
    cart = Cart.objects.get(id=card_id)
    
    words = Word.objects.filter(cart=cart)
    
    return render_to_response('linew_litvinov/card.html', locals(), context)

@login_required
def my_profile(request):
    context = RequestContext(request)
    
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    carts = user_profile.carts.all()
    
    return render_to_response('linew_litvinov/my_profile.html', locals(), context)
    
@login_required
def add_card(request, card_id):
    context = RequestContext(request)
    
    cart = Cart.objects.get(id=card_id)
    
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    
    carts = user_profile.carts.all()
    
    if not cart in carts:
        user_profile.carts.add(cart)
        user_profile.save()
    
    return HttpResponseRedirect(reverse('cards'));

def see_card(request, card_id, i, direction):
    context = RequestContext(request)
    
    i = int(i)
    direction = int(direction)
    
    if direction == -1:
        i = i - 1
    elif direction == 1:
        i = i + 1
    
    cart = Cart.objects.get(id=card_id)
    
    words = cart.word_set.all()
    
    
    if i >= len(words):
        i = 0
    if i < 0:
        i = len(words) - 1
        
    print i
    word = words[i]
    print word.english_word
    
    return render_to_response('linew_litvinov/see_card.html', locals(), context)


@login_required
def train_card(request, card_id):
    context = RequestContext(request)
    
    cart = Cart.objects.get(id=card_id)
    words = cart.word_set.all()
    
    try:
        train = TrainGame1.objects.get(user=request.user)
    except:
        train = TrainGame1(user=request.user, score=0, cart=cart, stage=0)
        train.save()
    
    if request.method == "POST":
        user_word = request.POST['user_word']
        if user_word == train.current_word.english_word:
            train.score += 1
            print "right"
        else:
            print "none"
        word = words[train.stage]
        train.stage += 1
        
    else:
        word = words[0]
    train.current_word = word
    guess_words = []
    import random
    for k in range(3):
        j = random.randint(0, len(words) - 1)
        while train.stage == j:
            j = random.randint(0, len(words) - 1)
        guess_words.append(words[j])
    return render_to_response('linew_litvinov/train_card.html', locals(), context)


def slider_card(request, card_id):
    context = RequestContext(request)
    
    cart = Cart.objects.get(id=card_id)
    words = cart.word_set.all()
    
    return render_to_response('linew_litvinov/slider_card.html', locals(), context)


def themes(request):
    context = RequestContext(request)
    
    themes = ThemeImages.objects.all()[:15]
    
    return render_to_response('linew_litvinov/themes.html', locals(), context)

def theme_cards(request, theme_id):
    context = RequestContext(request)
    
    theme = Theme.objects.filter(id=theme_id)[0]
    
    cards = Cart.objects.filter(theme=theme)
    
    words = cards[0].word_set.all()[:4]
    
    
    return render_to_response('linew_litvinov/theme_cards.html', locals(), context)


    
    
    