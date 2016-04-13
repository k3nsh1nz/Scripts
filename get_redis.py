#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import threading
from time import time
import redis
from prettytable import PrettyTable

'''
@author: k
'''

f = open("user_nhattao.txt",'a')
r = redis.StrictRedis(host='localhost', port=6379, db=0)
table = PrettyTable(["id","username"])
for i in range(1,100):
	table.add_row([i,r.get(i)])

f.write(table.get_string())