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

# Determine working directory
WORKING_DIRECTORY = os.getcwd()

REQUEST_HANDLER_CLASS = None # Must be redefined later !!

SERVER_PORT = 8080

SERVER_TITLE = "A.Bond's python server v0.07"

# Convert relative path to absolute
def rel2absPath(relpath):
	if relpath[0] == '/':
		relpath = relpath[1:]
	return os.path.join(WORKING_DIRECTORY,relpath)

# Something like execfile() but in global context.
def loadFile(fp):
	print 'Loading file: %s'%(fp)
	try:
		f = open(fp,'r')
		exec(f,globals()) # Function definitions don't work if 'globals' argument isn't set.
		f.close()
	except Exception as e:
		print '!!! Exception while loading file %s'%(fp)
		print e
		return False
	return True

# Execute multiple files from directory
def loadFiles(path=None,relative=None,cond=None):
	if path == None:
		path = rel2absPath(relative)
	filelist = os.listdir(path)
	for x in filelist:
		if cond != None:
			if not cond(x):
				continue
		loadFile(os.path.join(path,x))

# Load modules
loadFile('templates.py')
loadFile('server-handler.py')
loadFile('filecache.py')
loadFile('db-connection.py')

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

closeDBConnections( )

sys.stdout.flush()
sys.stderr.flush()
