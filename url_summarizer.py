# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests

fs = FrequencySummarizer()

def getTextFromURL(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)

#url = input("Enter a URL\n")
url = 'https://ischool.syr.edu/infospace/2017/03/20/android-security-can-go-wrong/'
final_summary = summarizeURL(url, 5)
print(final_summary.encode('ascii', 'ignore'))
for k in fs.keywords():
	print('{}: {}%'.format(k[0], k[1]*100))