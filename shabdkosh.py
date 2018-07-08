#!/usr/bin/python2

import os, sys, json, random
import requests
from bs4 import BeautifulSoup
from colorama import Fore,Back,Style,init

init(autoreset=True)

def write_history(word):
	resp = requests.get("https://www.vocabulary.com/dictionary/definition.ajax?search="+word+"&lang=en").text
	meaning = ''
	soup = BeautifulSoup(resp,"lxml")
	if soup.find("p",class_="short")!=None:
		meaning = soup.find("p",class_="short").text
	resp = requests.get("https://www.google.co.in/async/dictw?vet=10ahUKEwiJ8eflzKbbAhUcSI8KHcfkAowQg4MCCCgwAA..i&ved=0ahUKEwiJ8eflzKbbAhUcSI8KHcfkAowQu-gBCCwwAA&safe=off&yv=3&oq="+word+"&gs_l=dictionary-widget.1.0.0l2.81012.82436.0.84015.7.7.0.0.0.0.437.1861.2-5j1j1.7.0....0....1.64.dictionary-widget..0.7.1860....0.qABzZkKvdxY&async=term:"+word+",corpus:en,hhdr:true,hwdgt:true,wfp:true,xpnd:true,ttl:,tsl:en,ftclps:false,_id:dictionary-modules,_pms:s,_fmt:pc").content
	googsoup = BeautifulSoup(resp,"lxml")
	sen=[]
	if googsoup.find("div",class_="vmod") is not None:
		maindiv = googsoup.find("div",class_="lr_dct_ent")
		sen = maindiv.find_all("div",{"data-dobid":"dfn"})
	sen = [i.text for i in sen]

	with open(os.path.dirname(__file__)+"/.shabdkosh.json","r") as f:
		history = json.load(f)

	if word not in history.keys():
		history[word]={"vocab":meaning,"goog":sen}


	with open(os.path.dirname(__file__)+"/.shabdkosh.json","w") as f:
		json.dump(history,f)
	f.close()




def print_autocomplete(word):
	'''
	This method gets autocomplete words from vocabulary.com api
	'''
	soup = BeautifulSoup(requests.get("https://www.vocabulary.com/dictionary/autocomplete?search="+word).text,"lxml")
	words = soup.find_all("span",class_="word")
	definitions = soup.find_all("span",class_="definition")
	for (w,d) in zip(words,definitions):
		print Style.BRIGHT+Fore.GREEN+w.text," : ",d.text

def get_random_word():
	'''
	This method gets random word from vocabulary.com api
	'''
	return requests.get("https://www.vocabulary.com/randomword.json").json()['result']

def get_examples(word):
	'''
	This method gets examples of word from vocabulary.com corpus
	'''
	examples_json = requests.get("https://corpus.vocabulary.com/api/1.0/examples.json?query="+word+"&maxResults=50&startOffset=0&filter=0&_=1527055684693").json()
	if len(examples_json['result']['sentences'])>0:
		for i in range(len(examples_json['result']['sentences']))[:3]:                               # show first 3 example sentences
			print examples_json['result']['sentences'][i]['sentence'].encode('utf-8')
			if 'locator' in examples_json['result']['sentences'][i]['volume']:
				print examples_json['result']['sentences'][i]['volume']['locator'].encode('utf-8')," - ",examples_json['result']['sentences'][i]['volume']['corpus']['name'].encode('utf-8')
			print "\n"


def google_definition(word):
	content = requests.get("https://www.google.co.in/async/dictw?vet=10ahUKEwiJ8eflzKbbAhUcSI8KHcfkAowQg4MCCCgwAA..i&ved=0ahUKEwiJ8eflzKbbAhUcSI8KHcfkAowQu-gBCCwwAA&safe=off&yv=3&oq="+word+"&gs_l=dictionary-widget.1.0.0l2.81012.82436.0.84015.7.7.0.0.0.0.437.1861.2-5j1j1.7.0....0....1.64.dictionary-widget..0.7.1860....0.qABzZkKvdxY&async=term:"+word+",corpus:en,hhdr:true,hwdgt:true,wfp:true,xpnd:true,ttl:,tsl:en,ftclps:false,_id:dictionary-modules,_pms:s,_fmt:pc").content
	googsoup = BeautifulSoup(content,"lxml")
	sen=[]
	if googsoup.find("div",class_="vmod") is not None:
		maindiv = googsoup.find("div",class_="lr_dct_ent")
		sen = maindiv.find_all("div",{"data-dobid":"dfn"})
	for i in sen:
		print Style.BRIGHT+Fore.YELLOW+'> '+Style.RESET_ALL+i.text


def get_definition(word,ln):
	return requests.get("https://www.vocabulary.com/dictionary/definition.ajax?search="+word+"&lang="+ln)


def print_randomword_fromhistory():
	with open(os.path.dirname(__file__)+"/.shabdkosh.json","r") as f:
		history = json.load(f)
		randomkey = random.choice(history.keys())
		meantext=''
		for word in history[randomkey]["vocab"].split(" "):
				if word.lower().find(randomkey.lower())!=-1:
					meantext+= Style.BRIGHT+Fore.GREEN+word+" "+Style.RESET_ALL
				else:
					meantext+= word+" "+Style.RESET_ALL
		print meantext
		print "\n"
		for i in history[randomkey]["goog"]:
			print Style.BRIGHT+Fore.YELLOW+'> '+Style.RESET_ALL+i
	print "\n\n"
	f.close()

if __name__=='__main__':

	if len(sys.argv)==1:
		randomword = get_random_word()
		print Fore.WHITE+Back.BLACK+randomword['word']+Style.RESET_ALL

		soup = BeautifulSoup(get_definition(randomword['word'],randomword['lang']).text,"lxml")
		meaning = soup.find("p",class_="short").text.split(" ")
		meantext = ''
		for word in meaning:
			if word.lower().find(randomword['word'].lower())!=-1:
				meantext+= Style.BRIGHT+Fore.GREEN+word+" "+Style.RESET_ALL
			else:
				meantext+= word+" "+Style.RESET_ALL
		print meantext.encode('utf-8')
		print "\n"
		google_definition(randomword['word'])
		print "\n"
		get_examples(randomword['word'])

	else:
		if sys.argv[1]=="--history":
			print_randomword_fromhistory()


		else:
			print Fore.WHITE+Back.BLACK+sys.argv[1]+Style.RESET_ALL
			soup = BeautifulSoup(get_definition(sys.argv[1],"en").text,"lxml")
			if soup.find("p",class_="short")!=None:
				write_history(sys.argv[1])
				meaning = soup.find("p",class_="short").text.split(" ")
				meantext = ''
				for word in meaning:
					if word.lower().find(sys.argv[1].lower())!=-1:
						meantext+= Style.BRIGHT+Fore.GREEN+word+" "+Style.RESET_ALL
					else:
						meantext+= word+" "+Style.RESET_ALL
				print meantext.encode('utf-8')
				print "\n"
				google_definition(sys.argv[1])
				print "\n"
				get_examples(sys.argv[1])
			else:
				print_autocomplete(sys.argv[1])

