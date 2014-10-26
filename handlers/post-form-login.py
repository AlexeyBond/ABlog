# coding=UTF-8


@POSTRequestHandler('^/login$')
@POSTRequestHandler('^/login?from=',redirect=True)
def post__login(handler,redirect=False,**kwargs):
	form = handler.do_POST_parse_form( )
	if 'login' in form:
		login = form['login'].value
		if 'password' in form:
			password = form['password'].value
			uid = makeDBRequest('AUTHENTICATE-USER',
				username=login,passwd=password)
			if uid != None:
				print '',login,':',password,' logged in as user#',uid
			else:
				print 'Invalid login/password: ',login,':',password
		else:
			print 'no password'
	else:
		print 'no login'
	redirect_location = '/home' if redirect == False else handler.path[11:]
	handler.do_GET_REDIRECT(redirect_location)
