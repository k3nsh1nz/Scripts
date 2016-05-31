#!/usr/bin/python3

import http.client
import json
import sys

def getLink(username, password, link):
	conn = http.client.HTTPSConnection("api2.fshare.vn")
	conn.request("POST", "/api/user/login",
		"{\"app_key\":\"L2S7R6ZMagggC5wWkQhX2+aDi467PPuftWUMRFSn\""+
		",\"user_email\":\"" + username + "\"" + 
		",\"password\":\"" + password + "\"}")
	r = conn.getresponse()

	if r.status != 200:
		print("loi1")
		return None

	cookie = r.getheader("Set-Cookie")
	body = r.read()
	token = json.loads(body.decode('utf-8'))['token']

	conn.request("POST", "/api/Session/download", 
	"{\"url\":\"" + link + "\"" + 
	",\"token\":\"" + token + "\"}",{"Cookie" : cookie})
	r = conn.getresponse()

	if r.status != 200:
		print("loi2")
		return None

	body = r.read()
	return json.loads(body.decode('utf-8'))['location']	


if __name__ == '__main__':
	if len(sys.argv) < 4:
		print("Usage: " + sys.argv[0] + " username password link\n")
	else:
		link = getLink(sys.argv[1], sys.argv[2], sys.argv[3])
		if link == None:
			print("Link khong ton tai hoac nhap sai\n")
		else: 
			print("Link download: " + link + "\n")
