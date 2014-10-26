# coding=UTF-8

import re

RESOURCE_PATH_VALIDATION_EXPRESSION = re.compile('(\.\.)|(//)|(\$)')

@GETRequestHandler('^/resource/.*')
def get__resource(handler,**kwargs):
	global RESOURCE_PATH_VALIDATION_EXPRESSION
	global FILE_CACHE
	global WORKING_DIRECTORY
	if RESOURCE_PATH_VALIDATION_EXPRESSION.search(handler.path) != None:
		handler.start_response(200)
		renderPageTemplate('ERROR_BAD_RESOURCE_PATH',handler.wfile)
		return
	fullpath = rel2absPath(handler.path)
	data,mime = FILE_CACHE.getFile(fullpath)
	if data != None:
		handler.start_response(200,content_type=mime[0],charset=mime[1])
		handler.wfile.write(data)
	else:
		handler.do_GET_404( )
