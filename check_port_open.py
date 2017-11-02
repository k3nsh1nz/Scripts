#/usr/bin/python

import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

def check_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip,port))
    if result == 0:
        print "IP: %s | port %d OPEN" %(ip,port)
    else:
        print 'IP: %s | port %d CLOSED, connect_ex: %s' %(ip,port,str(result))

def main():
    check_port(ip,port)

if __name__ == '__main__':
    main()
