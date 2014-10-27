#!/usr/bin/python
# coding=UTF-8

# Imports
import threading
import cgi
import os
import sys

# Import & init mimetypes
import mimetypes
mimetypes.init()

# More imports
import BaseHTTPServer
import SocketServer

# Load ab_utils.py
execfile('./ab_utils.py',globals())

SERVER_REQUEST_HANDLER_CLASS = None # Must be redefined later !!

SERVER_PORT = 8080

SERVER_TITLE = "A.Bond's python server v0.07"

# Load modules
loadModuleGroup('MODULES','modules')

# Server class
class ThreadedHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
	"""Handle requests in a separate thread."""

# Server run procedure
def runServer( ):
	global SERVER_PORT
	global REQUEST_HANDLER_CLASS
	try:
		srv = ThreadedHTTPServer(('', SERVER_PORT), REQUEST_HANDLER_CLASS)
		print 'Starting server ...'
		srv.serve_forever()
	except KeyboardInterrupt:
		print '\r!!! Keyboard interrupt. Server stopped.'
	except Exception, e:
		raise e

print 'WORKING_DIRECTORY = ', WORKING_DIRECTORY

runServer( )

onShutdown( )
