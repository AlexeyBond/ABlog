# coding=UTF-8

@GETRequestHandler('^/src/view\\?',template='SRCVIEW_FILE',parse_url_args=True)
@GETRequestHandler('^/src$',template='SRCVIEW_ROOT')
@GETRequestHandler('^/src/tree$',template='SRCVIEW_TREE')
@GETRequestHandler('^/posts',template='VIEW-POSTS',parse_url_args=True)
@GETRequestHandler('^/home',template='HOMEPAGE')
@GETRequestHandler('^/login',template='LOGIN-PAGE',parse_url_args=True)
@GETRequestHandler('^/about',template='ABOUTPAGE')
@GETRequestHandler('^/new$',template='NEW-POST')
@GETRequestHandler('^/register',template='REGISTER-PAGE',parse_url_args=True)
def get__template(handler,template,parse_url_args=False,**kwargs):
	url_args = parseUrlParameters(handler.path) if parse_url_args else None
	session = makeDBRequest('IDENTIFY-USER-BY-COOKIES',cookies=handler.cookies)
	#
	if session != None:
		print 'Session detected: ',session['user_name'],'(id',session['user_id'],')'
	# 
	handler.start_response(200)
	renderPageTemplate(template,handler.wfile,session=session,handler=handler,url_args=url_args,**kwargs)

@GETRequestHandler('^/$',location='/home')
def get__redirect(handler,location,**kwargs):
	handler.do_GET_REDIRECT(location)

