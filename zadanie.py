#!/usr/bin/python
# -*- coding: utf-8 -*
# encoding= utf-8
 
import re
import urllib2
from nltk.tokenize import sent_tokenize

#czyszczenie plikow
open('./en.txt', 'w').write("")
open('./hr.txt', 'w').write("")
open('./test.txt', 'w').write("")
open('./en2.txt', 'w').write("")



#WYSZUKIWANIE LINKOW EN
path = 'en_links.txt'
en_file = open(path,'r')
en_links= []
en_sent = []
lines = en_file.readlines()
en_ok = []
hr_ok = []


for line in lines:
	text=line.split()
	for link in text:
		en_links += re.findall(r"<loc>(.*)</loc>", link)


for link in en_links:
	response =urllib2.urlopen(link)
	page_source = response.read()
	page = re.findall(r"<p[\w\s=\"]*>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;− ]*)</p>", page_source)
	page2 = re.findall(r"<figcaption>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−– ]*)</figcaption>", page_source)
	page3 = re.findall(r"<p[\w\s=\"]*>\n*([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéèü€É<>/:;?!’–»«×”“…²\&nbsp;− ]*)</p>", page_source)
	page4 = re.findall(r"<p[\w\s=\"]*>\n*([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéèü€É<>/:;?!’–»«×”“…²\&nbsp;− ]*)<a href=.*>.*</a></p>", page_source)
	en_sent.append(page)
	en_sent.append(page2)
	en_sent.append(page4)

licznik = 0

for line in en_sent:
	for line2 in line:
		licznik += 1
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		en_ok.append(line_en_change)


licz = 1
for p in en_ok:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list = sent_tokenize(source)
	for k2 in sent_tokenize_list:
		if(k2!=''):
			licz += 1
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")

###################################################################################################################3

path2 = 'hr_links.txt'
hr_file = open(path2,'r')
hr_links= []
hr_sent = []	
lines2 = hr_file.readlines()

for line2 in lines2:
	text2=line2.split()
	for link2 in text2:
		hr_links += re.findall(r"<loc>(.*)</loc>", link2)



for link in hr_links:
	response =urllib2.urlopen(link)
	page_source2 = response.read()
	page = re.findall(r"<p[\w\s=\"]*>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*)</p>", page_source2)
	page2 = re.findall(r"<figcaption>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*)</figcaption>", page_source2)
	page3 = re.findall(r"<p[\w\s=\"]*>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“²\&nbsp;−  ]*)\n</p>", page_source2)
	page4 = re.findall(r"<p[\w\s=\"]*>\n*([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéèü€É<>/:;?!’–»«×”“…²\&nbsp;− ]*)<a href=.*>.*</a></p>", page_source2)
	hr_sent.append(page)
	hr_sent.append(page2)
	hr_sent.append(page4)

licznik = 0
for line in hr_sent:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)	
		hr_ok.append(line_en_change)

licz = 1
for p in hr_ok:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list = sent_tokenize(source)
	for k2 in sent_tokenize_list:
		if(k2!=''):
			licz += 1
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")

##################################################################################################################################
##################################################################################################################################

path = 'pula_links.xml'
pula_file = open(path,'r')
pula_links = []
pula_sent = []	
pula_ok = [] 
lines = pula_file.readlines()

istra_path = 'istra_links.xml'
istra_file = open(istra_path, 'r')
istra_sent = []
istra_ok = []
istra_links = []
istra_lines = istra_file.readlines()

path_hr = 'pula_links_hr.xml'
pula_file_hr = open(path_hr,'r')
pula_links_hr = []
pula_sent_hr = []	
pula_ok_hr = [] 
lines_hr = pula_file_hr.readlines()

istra_path_hr = 'istra_links_hr.xml'
istra_file_hr = open(istra_path_hr, 'r')
istra_sent_hr = []
istra_ok_hr = []
istra_links_hr = []
istra_lines_hr = istra_file_hr.readlines()

for line in lines:
	text=line.split()
	for link in text:
		pula_links += re.findall(r"<loc>(.*)</loc>", link)

for line in istra_lines:
	text=line.split()
	for link in text:
		istra_links += re.findall(r"<loc>(.*)</loc>", link)


for link in pula_links:
	site = link

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}

	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*)</p>", content)###
	pula_sent.append(page)

for link in istra_links:
	site = link

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	
	page3 = re.findall(r"<div[\w\s\=\"]+><p>([^0-9-].*)</p>", content)
	page = re.findall(r"<strong>([^0-9-].*)</strong>", content)
	istra_sent.append(page3)
	istra_sent.append(page)

licznik = 0
for line in pula_sent:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Cultural sights|Entertainment|Information:|10 Best Wine Travel Destinations 2015|World's 2nd Best Olive Oil Region 2010 - 2015|Top 10 Valentine's Day Retreats 2014|Best Wine Regions for Winter and Spring Travel 2014|Best Olive Oil Region in the world 2016 and 2017|10 Best European <br>Wine Destinations 2016|10 Best Wine Travel Destinations 2015|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		pula_ok.append(line_en_change)

for line in istra_sent:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|<!---->|<a class=|Cultural sights|Entertainment|&nbsp;|Information:|10 Best Wine Travel Destinations 2015|World's 2nd Best Olive Oil Region 2010 - 2015|Top 10 Valentine's Day Retreats 2014|Best Wine Regions for Winter and Spring Travel 2014|Best Olive Oil Region in the world 2016 and 2017|10 Best European <br>Wine Destinations 2016|10 Best Wine Travel Destinations 2015|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		istra_ok.append(line_en_change)

for p in pula_ok:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list = sent_tokenize(source)
	for k2 in sent_tokenize_list:
		if(k2!=''):
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")

for p in istra_ok:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list = sent_tokenize(source)
	for k2 in sent_tokenize_list:
		if(k2!=''):
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")


########################################################################################
for line in lines_hr:
	text=line.split()
	for link in text:
		pula_links_hr += re.findall(r"<loc>(.*)</loc>", link)


for line in istra_lines_hr:
	text=line.split()
	for link in text:
		istra_links_hr += re.findall(r"<loc>(.*)</loc>", link)

for link in pula_links_hr:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*)</p>", content)###
	pula_sent.append(page)

for link in istra_links_hr:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page3 = re.findall(r"<div[\w\s\=\"]+><p>([^0-9-].*)</p>", content)
	page = re.findall(r"<strong>([^0-9-].*)</strong>", content)
	istra_sent_hr.append(page3)
	istra_sent_hr.append(page)

for line in pula_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Cultural sights|Entertainment|Information:|10 Best Wine Travel Destinations 2015|World's 2nd Best Olive Oil Region 2010 - 2015|Top 10 Valentine's Day Retreats 2014|Best Wine Regions for Winter and Spring Travel 2014|Best Olive Oil Region in the world 2016 and 2017|10 Best European <br>Wine Destinations 2016|10 Best Wine Travel Destinations 2015|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		pula_ok_hr.append(line_en_change)

for line in istra_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|<!---->|<a class=|Cultural sights|Entertainment|&nbsp;|Information:|10 Best Wine Travel Destinations 2015|World's 2nd Best Olive Oil Region 2010 - 2015|Top 10 Valentine's Day Retreats 2014|Best Wine Regions for Winter and Spring Travel 2014|Best Olive Oil Region in the world 2016 and 2017|10 Best European <br>Wine Destinations 2016|10 Best Wine Travel Destinations 2015|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		istra_ok_hr.append(line_en_change)

for p in pula_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)
	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")

for p in istra_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)
	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")


#######################################################################################################################
#######################################################################################################################

path_hr = 'top_links_hr.xml'
top_file_hr = open(path_hr,'r')
top_links_hr = []
top_sent_hr = []	
top_ok_hr = [] 
lines_hr = top_file_hr.readlines()

for line in lines_hr:
	text=line.split()
	for link in text:
		top_links_hr += re.findall(r"<loc>(.*)</loc>", link)

for link in top_links_hr:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>(.*)</p>", content)
	top_sent_hr.append(page)

for line in top_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Cultural sights|Entertainment|Information:|10 Best Wine Travel Destinations 2015|World's 2nd Best Olive Oil Region 2010 - 2015|Top 10 Valentine's Day Retreats 2014|Best Wine Regions for Winter and Spring Travel 2014|Best Olive Oil Region in the world 2016 and 2017|10 Best European <br>Wine Destinations 2016|10 Best Wine Travel Destinations 2015|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		top_ok_hr.append(line_en_change)

for p in top_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)
	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")

#####################################################################################################

path_en = 'top_links_en.xml'
top_file_en = open(path_en,'r')
top_links_en = []
top_sent_en = []
top_ok_en = [] 
lines_en = top_file_en.readlines()

for line in lines_en:
	text=line.split()
	for link in text:
		top_links_en += re.findall(r"<loc>(.*)</loc>", link)

for link in top_links_en:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>(.*)</p>", content)
	top_sent_en.append(page)

for line in top_sent_en:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Cultural sights|Entertainment|Information:|10 Best Wine Travel Destinations 2015|World's 2nd Best Olive Oil Region 2010 - 2015|Top 10 Valentine's Day Retreats 2014|Best Wine Regions for Winter and Spring Travel 2014|Best Olive Oil Region in the world 2016 and 2017|10 Best European <br>Wine Destinations 2016|10 Best Wine Travel Destinations 2015|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		top_ok_en.append(line_en_change)

for p in top_ok_en:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_en = sent_tokenize(source)
	for k2 in sent_tokenize_list_en:
		if(k2!=''):
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")


##############################################################################################################################################
##############################################################################################################################################

path_hr = 'medulin_links_hr.xml'
top_file_hr = open(path_hr,'r')
top_links_hr = []
top_sent_hr = []	
top_ok_hr = [] 
lines_hr = top_file_hr.readlines()

for line in lines_hr:
	text=line.split()
	for link in text:
		top_links_hr += re.findall(r"<loc>(.*)</loc>", link)

for link in top_links_hr:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*</div>)", content)
	top_sent_hr.append(page)

for line in top_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Medulin|<br>|Banjole|Premantura|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		top_ok_hr.append(line_en_change)

for p in top_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)
	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")

######################################################################################################################

path_en = 'medulin_links_en.xml'
top_file_en = open(path_hr,'r')
top_links_en = []	
top_sent_en = []	
top_ok_en = [] 
lines_en = top_file_en.readlines()

for line in lines_en:
	text=line.split()
	for link in text:
		top_links_en += re.findall(r"<loc>(.*)</loc>", link)

for link in top_links_en:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*</div>)", content)
	top_sent_en.append(page)

for line in top_sent_en:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Medulin|<br>|Banjole|Premantura|[-]*[0-9]&deg; - [-]*[0-9]&deg;|Plan your trip|Follow us:|All rights reserved &copy; 2017 Turistička zajednica grada Pule|Menu|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		top_ok_en.append(line_en_change)

for p in top_ok_en:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_en = sent_tokenize(source)
	for k2 in sent_tokenize_list_en:
		if(k2!=''):
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")

################################################################################################################################
################################################################################################################################

path_hr = 'visit_links_hr.xml'
visit_file_hr = open(path_hr,'r')
visit_links_hr = []	
visit_sent_hr = []	
visit_ok_hr = [] 
lines_hr = visit_file_hr.readlines()


for line in lines_hr:
	text=line.split()
	for link in text:
		visit_links_hr += re.findall(r"<loc>(.*)</loc>", link)

for link in visit_links_hr:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*</p>)", content)
	visit_sent_hr.append(page)

for line in visit_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Adresa: ULICA I GRAD|Prijavite se za newsletter i ne propustite važne informacije.|Radno vrijeme: DANI, SATI|<br>|[-]*[0-9]&deg; - [-]*[0-9]&deg;|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		visit_ok_hr.append(line_en_change)

for p in visit_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)

	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")

########################################################################################################

path_en = 'visit_links_en.xml'
visit_file_en = open(path_en,'r')
visit_links_en = []	
visit_sent_en = []	
visit_ok_en = [] 
lines_en = visit_file_en.readlines()

for line in lines_en:
	text=line.split()
	for link in text:
		visit_links_en += re.findall(r"<loc>(.*)</loc>", link)

for link in visit_links_en:
	site = link
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()
	page = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;−  ]*</p>)", content)
	visit_sent_en.append(page)

for line in visit_sent_en:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Adresa: ULICA I GRAD|Prijavite se za newsletter i ne propustite važne informacije.|Radno vrijeme: DANI, SATI|<br>|[-]*[0-9]&deg; - [-]*[0-9]&deg;|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		visit_ok_en.append(line_en_change)

for p in visit_ok_en:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_en = sent_tokenize(source)
	for k2 in sent_tokenize_list_en:
		if(k2!=''):
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")


############################################################################################################################################
############################################################################################################################33

#WYSZUKIWANIE LINKOW EN
path_hr = 'infofazana_en.xml'
visit_file_hr = open(path_hr,'r')
visit_links_hr = []	#linki pula.hr
visit_sent_hr = []	
visit_ok_hr = [] #linki istra.hr
lines_hr = visit_file_hr.readlines()


for line in lines_hr:
	text=line.split()
	for link in text:
		visit_links_hr += re.findall(r"<loc>(.*)</loc>", link)


for link in visit_links_hr:
	site = link

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()

	page1 = re.findall(r"<p[ \w\s=\":;-]+>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;\&ldquo;\&rdquo;\&ndash;\&rsquo;\&eacute;−  ]*</p>)", content)
	page2 = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;\&ldquo;\&rdquo;\&ndash;\&rsquo;\&eacute;−  ]*</p>)", content)

	visit_sent_hr.append(page1)
	visit_sent_hr.append(page2)


#print(top_sent_hr)


#WYPISANIE OSOBNO KAZDEGO ELEMENTU LISTY PULA
for line in visit_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Prijavite se za newsletter i ne propustite važne informacije.|TEKST RESTORANA|ULICA I GRAD|Adresa|Radno vrijeme: DANI, SATI|<br>|[-]*[0-9]&deg; - [-]*[0-9]&deg;|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		visit_ok_hr.append(line_en_change)

#print(top_ok_hr)


#ZAMIANA TEKSTU NA ZDANIA ISTRA
for p in visit_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)
	#print(sent_tokenize_list)
	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./en.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./en.txt', 'a+').write("\n")


###############################################################################################################################################

#WYSZUKIWANIE LINKOW EN
path_hr = 'infofazana_hr.xml'
visit_file_hr = open(path_hr,'r')
visit_links_hr = []	#linki pula.hr
visit_sent_hr = []	
visit_ok_hr = [] #linki istra.hr
lines_hr = visit_file_hr.readlines()


for line in lines_hr:
	text=line.split()
	for link in text:
		visit_links_hr += re.findall(r"<loc>(.*)</loc>", link)


for link in visit_links_hr:
	site = link

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)
	page = urllib2.urlopen(req)
	content = page.read()

	page1 = re.findall(r"<p[ \w\s=\":;-]+>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;\&ldquo;\&rdquo;\&ndash;\&rsquo;\&eacute;−  ]*</p>)", content)
	page2 = re.findall(r"<p>([\s\w\-.,\'$%\(\)ČčĆćžžĐđŠšŽžéžèü€É<>/:;?!’–»«×”“…’‘²\&nbsp;\&ldquo;\&rdquo;\&ndash;\&rsquo;\&eacute;−  ]*</p>)", content)

	visit_sent_hr.append(page1)
	visit_sent_hr.append(page2)


#print(top_sent_hr)


#WYPISANIE OSOBNO KAZDEGO ELEMENTU LISTY PULA
for line in visit_sent_hr:
	for line2 in line:
		line_en_change = re.sub(r"<b>|</b>|<p>|</p>|<i>|</i>|<li>|</li>|&nbsp;|Prijavite se za newsletter i ne propustite važne informacije.|TEKST RESTORANA|ULICA I GRAD|Adresa|Radno vrijeme: DANI, SATI|<br>|[-]*[0-9]&deg; - [-]*[0-9]&deg;|<ul>|</ul>|<div>|</div>|<br />|<h2>|</h2>|<em>|</em>|<figcaption>|</figcaption>|<strong>|</strong>", "", line2)
		visit_ok_hr.append(line_en_change)

#print(top_ok_hr)


#ZAMIANA TEKSTU NA ZDANIA ISTRA
for p in visit_ok_hr:
	source = unicode(p, 'iso 8859-2')
	sent_tokenize_list_hr = sent_tokenize(source)
	#print(sent_tokenize_list)
	for k2 in sent_tokenize_list_hr:
		if(k2!=''):
			open('./hr.txt', 'a+').write(k2.encode("iso 8859-2"))
			open('./hr.txt', 'a+').write("\n")


###############################################################################################################################
###############################################################################################################################


