#!/usr/bin/python
import re
import urllib2

'''
@author: k

'''

f = open("user_nhattao.txt",'a')

def get_user(url):
	try:
		res = urllib2.urlopen(url)
		patten = ''
		for i in res:
			if re.search(r'<title>',i.strip()):
				patten = i.strip().split(" ")
	except Exception, e:
		patten = ''

	#return patten[0][7:]
	try:
		return patten[0][7:]
	except Exception, e:
		return ""

#last user: 22486699

for i in range(1,10):
	url = "https://nhattao.com/members/"+str(i)
	if get_user(url):
		f.write(get_user(url)+"\n")

f.close()
