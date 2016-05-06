#!/usr/bin/python
import re

#k

arr = []
def proccess_log(log):
	date = re.findall(r'(\d.+\/\d+)\s(\d+:\d+:\d+)',log)
	ip = re.findall(r'(\d+.\d+.\d+.\d+)]\s',log)
	rules = re.findall(r'Pattern\smatch\s"(.+):"',log)
	args = re.findall(r'at\s([a-zA-Z1-9:_-]+)',log)
	id = re.findall(r'id\s"(\d+)"',log)
	msg = re.findall(r'msg\s"([a-zA-Z1-9\s]+)',log)
	hostname = re.findall(r'\[hostname\s"([a-zA-Z1-9_-]+)',log)
	uri = re.findall(r'uri\s"(\/[a-zA-Z1-9\.]+)',log)
	arr.append(msg)

def main():
	file = open("modsec.log","r")
	for line in file:
		try:
			proccess_log(line)
		except Exception, e:
			raise e

	print arr

if __name__ == '__main__':
	main()
