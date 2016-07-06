#!/usr/bin/env python

import sys
import socket

args = sys.argv
ip = args[1]
port = int(args[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("1", (ip, port))
print "Packet sent to " + ip + " on port " + str(port)