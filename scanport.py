#!/usr/bin/python
import nmap
import argparse
import sys

# @k
#

#pip install python-nmap
#function scan 
def findTgst(subNet,port):
	nm = nmap.PortScanner()
	nm.scan(subNet,str(port))
	tgtHosts = []
	for host in nm.all_hosts():
		if nm[host].has_tcp(port):
			state = nm[host]['tcp'][port]['state']
			if state == 'open':
				print '[+] Found Target Host: ' + host
				tgtHosts.append(host)
	return tgtHosts

#main
def main():
	example = "use: python scanport445.py -H 192.168.1.1-254 -p 445"
	parser = argparse.ArgumentParser()
	parser.add_argument('-H', action='store', dest='ip',
                    help='IP subNet')
	parser.add_argument('-p', action='store', dest='port',
                    help='PortScanner')
	parser.add_argument('--version', action='version', version='%(prog)s 2.0')
	args = parser.parse_args()
	if len(sys.argv) < 4:
		print example
		return 1
	else:
		ip = str(args.ip)
		port = int(args.port)
		findTgst(ip,port)
		return 0
if __name__ == '__main__':
	sys.exit(main())
