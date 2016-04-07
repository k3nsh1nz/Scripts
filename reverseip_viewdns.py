#!/usr/bin/python
import sys
import json
import urllib2
from prettytable import PrettyTable
import argparse
import socket
#
#sudo pip install prettytable
#http://api.hackertarget.com/reverseiplookup/?q=domains.com

# api
API_KEY="449eba65aaad809b7aeb7895579a3044bfddd201"

# function get ip
def get_ips_for_host(host):
        try:
            ips = socket.gethostbyname(host)
        except socket.gaierror:
            ips=''
        return ips

#reverse ip function
def reverseip(host):
	url = urllib2.urlopen(host).read()
	result = json.loads(url)
	t = PrettyTable(['Domain', 'Last Resolved Date', 'IP'])
	for domain in result['response']['domains']:
		t.add_row([domain['name'], domain['last_resolved'], get_ips_for_host(domain['name'])])
	print t

#main
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-host', action='store', dest='host',
                    help='Domainname or IP Server')
	parser.add_argument('-o', action='store', dest='output',
                    help='Output: json or xml')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')
	results = parser.parse_args()

	if len(sys.argv) > 4:
		url = "http://pro.viewdns.info/reverseip/?host="+results.host+"&apikey="+API_KEY+"&output="+results.output
		reverseip(url)
	else:
		parser.print_help()

	return 1

if __name__ == '__main__':
	sys.exit(main())
