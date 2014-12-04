import os

from bs4 import BeautifulSoup
import urllib2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'english.settings')
from freq_words.models import Word

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
    