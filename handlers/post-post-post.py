# coding=UTF-8

@POSTRequestHandler('^/new')
def post__post(handler,**kwargs):
	session = makeDBRequest('IDENTIFY-USER-BY-COOKIES',cookies=handler.cookies)
	form = handler.do_POST_parse_form( )
	if session == None:
		if 'login' not in form or 'password' not in form:
			print 'No login or password'
			handler.do_GET_REDIRECT('/login?from=/new&error=1')
			return
		login = form['login'].value
		password = form['password'].value
		#
		if (REGEXP_VALID_LOGIN.search(login) == None or 
			REGEXP_VALID_PASSWORD.search(password) == None):
			print 'Bad username/password ',login,':',password
			handler.do_GET_REDIRECT('/login?from=/new&error=1')
			return
		#
		userid = makeDBRequest('AUTHENTICATE-USER',username=login,passwd=password)
		if userid == None:
			print 'Invalid username/password ',login,':',password
			handler.do_GET_REDIRECT('/login?from=/new&error=1')
			return
		session={'user_id':userid}
	#
	text = form['post_text'].value if 'post_text' in form else '. . .'
	makeDBRequest('NEW-POST',userid=session['user_id'],posttext=text)
	#
	handler.do_GET_REDIRECT('/posts')
