#!/usr/bin/python
#
#bruce force hash password md5
#dict: https://onedrive.live.com/redir?resid=F8468E56B9F32DFA!29870&authkey=!ADETMCy4NZFwjUI&ithint=file%2czip
#

import re
import hashlib
password = open("passwd.txt").read()
cleartext = open("6tr-user-vn-zoom.txt")
for i in cleartext:
	m = hashlib.md5()
	m.update(i.strip())
	if re.search(m.hexdigest(),password):
		print m.hexdigest()+":"+i.strip()
