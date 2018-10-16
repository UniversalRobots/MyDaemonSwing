#!/usr/bin/env python

import time
import sys

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

title = ""

def set_title(new_title):
	global title
	title = new_title
	return title

def get_title():
	tmp = ""
	if str(title):
		tmp = title
	else:
		tmp = "No title set"
	return tmp + " (Python)"

def get_message(name):
	if str(name):
		return "Hello " + str(name) + ", welcome to PolyScope!"
	else:
		return "No name set"

sys.stdout.write("MyDaemon daemon started")
sys.stderr.write("MyDaemon daemon started")

server = SimpleXMLRPCServer(("127.0.0.1", 40405))
server.register_function(set_title, "set_title")
server.register_function(get_title, "get_title")
server.register_function(get_message, "get_message")
server.serve_forever()

