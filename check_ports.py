#!/usr/bin/env python

""" Test for opened ports
By Nicola Senno

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from optparse import OptionParser
from socket import *
import sys

def is_valid(port):
    try:
        return 1 <= int(port) <= 65535
    except ValueError:
        return False


def port_test(ip, port):

    # Define a new socket
    s = socket(AF_INET, SOCK_STREAM)

    # Open the connection
    result = s.connect_ex((ip, port))

    # Close the connection
    s.close()

    if result == 0:
        return 0
    return 1


def check(ip, ports):
    status = 0
    status_string = ['OK','WARNING','CRITICAL']
    totals = {0: [], 1: []}

    for port in ports:
        st = port_test(ip, int(port))
        totals[st].append(port)
        if st == 1 and not status > 0:
            status = 2

    print "%s; ports opened %s - ports closed %s" % (status_string[status],
                                                    ",".join(totals[0]),
                                                    ",".join(totals[1]),)
    return status


if __name__ == "__main__":
    parser = OptionParser(
        usage="%prog [-o <IP> -p <[PORTS]> -t <TIMEOUT>]",
        version="%prog $Revision$",
        prog="check_ports",
        description="""This program makes a check if the given 
        ports are opened or closed
        """,
    )
    parser.add_option(
        "-o",
        "--host",
        action="store",
        type="string",
        dest="hosts",
        default=None,
        help="Host to connect to. [default: %default]",
    )
    parser.add_option(
        "-p",
        "--ports",
        action="store",
        type="string",
        dest="ports",
        default=None,
        help="Port to connect on. [default: %default]",
    )

    parser.add_option(
        "-t",
        "--timeout",
        action="store",
        type="int",
        dest="timeout",
        default=5,
        help="Timeout connection. [default: %default]",
    )

    (opts, args) = parser.parse_args()

    if not opts.hosts:
        parser.error("Host or ip is missing")

    if not opts.ports:
        parser.error("Port number is missing")

    ports = [port for port in opts.ports.split(",")
             if is_valid(port)]

    if len(ports) < len(opts.ports.split(",")):
        parser.error("One of the given ports is not in 1 <= port <= 65535")

    setdefaulttimeout(opts.timeout)
    status = check(opts.hosts, ports)
    sys.exit(status)

