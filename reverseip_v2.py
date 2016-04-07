#!/usr/bin/python
import sys
import json
import urllib2
from prettytable import PrettyTable
import argparse
import socket
#
#sudo pip install prettytable

# function get ip
def get_ips_for_host(host):
        try:
            ips = socket.gethostbyname(host)
        except socket.gaierror:
            ips=''
        return ips

#reverse ip function
def reverseip(host):
	url = urllib2.urlopen(host)
	t = PrettyTable(['Domain', 'IP'])
	for domain in url:
		domain = domain.strip()
		t.add_row([domain,get_ips_for_host(domain)])
	print t

#main
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-host', action='store', dest='host',
                    help='Domainname or IP Server')
	parser.add_argument('--version', action='version', version='%(prog)s 2.0')
	args = parser.parse_args()

	if len(sys.argv) > 2:
		url = "http://api.hackertarget.com/reverseiplookup/?q="+args.host
		reverseip(url)
	else:
		parser.print_help()

	return 1

if __name__ == '__main__':
	sys.exit(main())
