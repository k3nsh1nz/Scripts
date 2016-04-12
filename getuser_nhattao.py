#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib2
import threading
from time import time
import redis

'''
@author: k
'''

#f1 = open("user_nhattao/user_nhattao1.txt",'a')
#f2 = open("user_nhattao/user_nhattao2.txt",'a')
r = redis.StrictRedis(host='localhost', port=6379, db=0)

start_time = time()

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
# def run_getuser(start_user,end_user,f_write):
# 	for i in range(start_user,end_user):
# 		url = "https://nhattao.com/members/"+str(i)
# 		if get_user(url):
# 			f_write.write(get_user(url)+"\n")
#---------------------
threads = []
for i in range(500,1500):
	url = "https://nhattao.com/members/"+str(i)
	t = threading.Thread(target=get_user, args=(url,))
	if t:
		threads.append(t)
		t.start()
		r.set(i,get_user(url))

#---------------------
# for i in range(1,500):
# 	url = "https://nhattao.com/members/"+str(i)
# 	if get_user(url):
# 		f2.write(get_user(url)+"\n")

end_time = time()
time_process = end_time - start_time
print "Time time process: ", time_process
# 
#threading.Thread(target=run_getuser,args=(5000, 5500, f1),).start()

