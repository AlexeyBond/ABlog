# coding=UTF-8

@POSTRequestHandler('^/register')
def post__register(handler,**kwargs):
	form = handler.do_POST_parse_form( )
	if 'login' not in form:
		handler.do_GET_REDIRECT('/register?login_incorrect=1')
		return
	if REGEXP_VALID_LOGIN.search(form['login'].value) == None:
		handler.do_GET_REDIRECT('/register?login_incorrect=1')
		return
	login = form['login'].value
	#
	uinfo = makeDBRequest('GET-USER-ID-BY-NAME',name=login)
	if uinfo != None:
		handler.do_GET_REDIRECT('/register?login_in_use=1&login='+login)
		return
	#
	if ('password' not in form) or ('password_repeat' not in form):
		handler.do_GET_REDIRECT('/register?password_incorrect=1&login='+login)
		return
	password = form['password'].value
	if password != form['password_repeat'].value:
		handler.do_GET_REDIRECT('/register?password_mismatch=1&login='+login)
		return
	makeDBRequest('NEW-USER',name=login,passwd=password)
	handler.do_GET_REDIRECT('/login?login='+login)
