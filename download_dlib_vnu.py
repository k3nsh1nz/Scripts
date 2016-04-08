#!/usr/bin/python
import re
import urllib2
import argparse
import os

#
# k
#

def getlink(url):
	res = urllib2.urlopen(url)
	patten = ""
	for i in res:
		if re.search(r"<img src=\"\/iii\/cpro\/app\?id=",i.strip()):
			patten = i.strip()


	id_search = re.search(r"app\?id=(\d+)", patten)
	sp_search = re.search(r"sp=(\d+)",url)

	result = "http://dlib.vnu.edu.vn/iii/cpro/app?id="+id_search.group(0)[7:]+"&itemId="+sp_search.group(0)[3:]+"&lang=vie&service=blob&suite=def"

	return result

def main():
	parser = argparse.ArgumentParser(description='test')
	parser.add_argument('-url', default=os.environ.get('URL', None))

	args = parser.parse_args()
	if not args.url:
	    exit(parser.print_usage())
	else:
		print "\nLink download :", (getlink(args.url))
if __name__ == '__main__':
	main()
