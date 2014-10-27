# coding=UTF-8


# Imports
import threading
import cgi
import os
import sys


# Determine working directory
WORKING_DIRECTORY = os.getcwd()


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
def loadFiles(path=None,relative=None):
	if path == None:
		path = rel2absPath(relative)
	filelist = os.listdir(path)
	for x in filelist:
		if x.endswith('.py'):
			loadFile(os.path.join(path,x))

#
MODULE_GROUPS = {}

#
def loadModuleGroup(name,relpath):
	global MODULE_GROUPS
	MODULE_GROUPS[name] = relpath
	print '---   Loading module group %s   ---'%(name)
	loadFiles(relative=relpath)
	print '--- End loading module group %s ---'%(name)

#
def reloadModuleGroup(name):
	global MODULE_GROUPS
	print '---   Reloading module group %s   ---'%(name)
	loadFiles(relative=MODULE_GROUPS[name])
	print '--- End reloading module group %s ---'%(name)

#
def setModuleGroupPath(name,path):
	global MODULE_GROUPS
	MODULE_GROUPS[name] = path

# List of procedures that should be called on
# server shutdown
SHUTDOWN_PROCEDURES = ()

# Decorator which adds a procedure to
# SHUTDOWN_PROCEDURES
def callOnShutdown(func):
	global SHUTDOWN_PROCEDURES
	SHUTDOWN_PROCEDURES = (func,)+SHUTDOWN_PROCEDURES
	return func

# Call the procedures that should be called
# on server shutdown
def onShutdown( ):
	global SHUTDOWN_PROCEDURES
	for proc in SHUTDOWN_PROCEDURES:
		try:
			proc()
		except Exception as e:
			print e

# Parse parameters from url or HTTP
# request path
def parseUrlParameters(url):
	parstart = url.find('?') + 1
	pardict = {}
	if parstart != 0:
		pars = url[parstart:].split('&')
		for par in pars:
			pair = par.split('=')
			if len(pair) != 2:
				continue
			pardict[pair[0]] = pair[1]
	return pardict

