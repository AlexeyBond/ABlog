# coding=UTF-8
import os
import sys

PAGE_TEMPLATES = {}

PAGE_TEMPLATES_COMMON_DIR_NAME = 'templates/common'
PAGE_TEMPLATES_DIR_NAME = 'templates'

# Аццкый ШАБЛОНИЗАТОР
def pageTemplate(templname):
	def writeObject(stream, obj):
		if type(obj).__name__ == 'generator':
			for x in obj:
				writeObject(stream,x)
		elif type(obj) is str:
			stream.write(obj)
		else:
			stream.write(str(obj))
	def pageTemplateDecorator(templfunc):
		global PAGE_TEMPLATES
		def templfuncWrapper(ostream,**kwargs):
			obj = templfunc(**kwargs)
			writeObject(ostream,obj)
		# Add template to list
		PAGE_TEMPLATES[templname] = templfuncWrapper
		print 'Loaded page template: %s'%(templname)
		return templfunc
	return pageTemplateDecorator
# Usage:
# @pageTemplate('HOMEPAGE')
# def myHomepageTemplate( **kwargs )
# 	yield '<!DOCTYPE html>'
#	yield '<html>'
#	. . .
# Or:
# @pageTemplate('HOMEPAGE')
# def myHomepageTemplate( **kwargs )
#	return """<html>
#	. . .
#	</html>"""

def renderPageTemplate(templname,ostream,**kwargs):
	global PAGE_TEMPLATES
	if templname not in PAGE_TEMPLATES:
		print 'Couldn\'t find template: %s'%(templname)
		return None
	return PAGE_TEMPLATES[templname](ostream,**kwargs)

loadModuleGroup('PAGE-TEMPLATES-COMMON',PAGE_TEMPLATES_COMMON_DIR_NAME)
loadModuleGroup('PAGE-TEMPLATES',PAGE_TEMPLATES_DIR_NAME)

