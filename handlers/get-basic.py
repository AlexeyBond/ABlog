# coding=UTF-8

@GETRequestHandler('^/src/view\\?',template='SRCVIEW_FILE',parse_url_args=True)
@GETRequestHandler('^/src$',template='SRCVIEW_ROOT')
@GETRequestHandler('^/src/tree$',template='SRCVIEW_TREE')
@GETRequestHandler('^/posts',template='VIEW-POSTS',parse_url_args=True)
@GETRequestHandler('^/home',template='HOMEPAGE')
@GETRequestHandler('^/about',template='ABOUTPAGE')
def get__template(handler,template,parse_url_args=False,**kwargs):
	url_args = parseUrlParameters(handler.path) if parse_url_args else None
	# 
	handler.start_response(200)
	renderPageTemplate(template,handler.wfile,handler=handler,url_args=url_args,**kwargs)

@GETRequestHandler('^/$',location='/home')
def get__redirect(handler,location,**kwargs):
	handler.do_GET_REDIRECT(location)

