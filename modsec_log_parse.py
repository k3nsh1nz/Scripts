#!/usr/bin/python
#@: k

import re
import MySQLdb

db = MySQLdb.connect("localhost","root","xxx","xxx")
cursor = db.cursor()

#parse log function
def proccess_log(log):
	date = ' '.join(re.findall(r'(\d.+\/\d+)\s(\d+:\d+:\d+)',log)[0])
	ip = ''.join(re.findall(r'(\d+.\d+.\d+.\d+)]\s',log)[0])
	rules = ''.join(re.findall(r'Pattern\smatch\s"(.+):"',log)[0])
	args = ''.join(re.findall(r'at\s([a-zA-Z1-9:_-]+)',log)[0])
	rules_id = ''.join(re.findall(r'id\s"(\d+)"',log)[0])
	msg = ''.join(re.findall(r'msg\s"([a-zA-Z1-9\s]+)',log)[0])
	hostname = ''.join(re.findall(r'\[hostname\s"([a-zA-Z1-9_-]+)',log)[0])
	uri = ''.join(re.findall(r'uri\s"(\/[a-zA-Z1-9\.]+)',log)[0])
	
	#insert log to mysql
	cursor.execute("INSERT INTO log(date,ip,rules,args,rules_id,msg,hostname,uri) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(date,ip,rules,args,int(rules_id),msg,hostname,uri))
	db.commit()

#main
def main():
	file = open("modsec.log","r")
	for line in file:
		try:
			proccess_log(line)
		except Exception, e:
			raise e

	#print arr

if __name__ == '__main__':
	main()
