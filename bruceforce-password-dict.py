#!/usr/bin/python
import re
import hashlib
password = open("passwd.txt").read()
cleartext = open("6tr-user-vn-zoom.txt")
for i in cleartext:
	m = hashlib.md5()
	m.update(i.strip())
	if re.search(m.hexdigest(),password):
		print m.hexdigest()+":"+i.strip()
