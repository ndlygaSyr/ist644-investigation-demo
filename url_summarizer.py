# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests


class URLSummarizer(object):

	page_title = ""

	def __init__(self):
		self.fs = FrequencySummarizer()

	def getTextFromURL(self, url):
		r = requests.get(url)
		soup = BeautifulSoup(r.text, "html.parser")
		self.page_title = soup.find("title").text
		text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
		return text

	def summarizeURL(self, url, total_sent):
		"""
		fs: FrequencySummarizer
		url: Site url
		total_pars: number of sentences to return 
		"""
		url_text = self.getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")
		final_summary = self.fs.summarize(url_text.replace("\n"," "), total_sent)
		return " ".join(final_summary)

	
	def get_keywords(self, num_words=10):
		"""
		Returns num of keywords from summarizer
		"""
		return self.fs.keywords(num_words)

	def get_page_title(self):
		return self.page_title
