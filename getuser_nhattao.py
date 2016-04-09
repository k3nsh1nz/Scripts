#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib2
import threading

'''
@author: k
'''

f1 = open("user_nhattao/user_nhattao1.txt",'a')
f2 = open("user_nhattao/user_nhattao2.txt",'a')
f3 = open("user_nhattao/user_nhattao3.txt",'a')
f4 = open("user_nhattao/user_nhattao4.txt",'a')
f5 = open("user_nhattao/user_nhattao5.txt",'a')
#f6 = open("user_nhattao/user_nhattao6.txt",'a')
#f7 = open("user_nhattao/user_nhattao7.txt",'a')

def get_user(url):
	try:
		res = urllib2.urlopen(url)
		patten = ''
		for i in res:
			if re.search(r'<title>',i.strip()):
				patten = i.strip().split(" ")
	except Exception, e:
		patten = ''

	try:
		return patten[0][7:]
	except Exception, e:
		return ""

#last user: 22486699
def run_getuser(start_user,end_user,f_write):
	for i in range(start_user,end_user):
		url = "https://nhattao.com/members/"+str(i)
		if get_user(url):
			f_write.write(get_user(url)+"\n")

# 
threading.Thread(
        target=run_getuser,
        args=(5000, 5500, f1),
    ).start()
threading.Thread(
        target=run_getuser,
        args=(5500, 6000, f2),
    ).start()
threading.Thread(
        target=run_getuser,
        args=(6000, 6500, f3),
    ).start()
threading.Thread(
        target=run_getuser,
        args=(6500, 7000, f4),
    ).start()
threading.Thread(
        target=run_getuser,
        args=(7000, 7500, f5),
    ).start()

