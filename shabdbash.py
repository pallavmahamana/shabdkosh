#!/usr/bin/python
import os,json,random
from colorama import Style,Fore
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
