# coding=UTF-8

def makeNewCookie(user_id,user_addr):
	cookieval = (
		str(int(time.time()*10000)) + '-' +
		str(user_addr[0]) + '-' +
		str(user_addr[1]) + '-' +
		str(user_id)
		)
	makeDBRequest('START-NEW-SESSION',user=user_id,cookie=cookieval)
	return cookieval

@POSTRequestHandler('^/login')
def post__login(handler,redirect=False,**kwargs):
	url_args = parseUrlParameters(handler.path)
	redirect_location = url_args['from'] if 'from' in url_args else '/home'
	redirect_headers = []
	form = handler.do_POST_parse_form( )
	if 'login' in form:
		login = form['login'].value
		if 'password' in form:
			password = form['password'].value
			uid = makeDBRequest('AUTHENTICATE-USER',
				username=login,passwd=password)
			if uid != None:
				cookie = makeNewCookie(uid,handler.client_address)
				print '',login,':',password,' logged in as user#',uid,'; setting cookie ',cookie
				redirect_headers.append(('Set-Cookie', 'sessionid='+cookie+'; path=/;'))
				redirect_headers.append(('Set-Cookie', 'userid='+str(uid)+'; path=/;'))
			else:
				print 'Invalid login/password: ',login,':',password
				redirect_location = '/login?error=1&from='+redirect_location+'&login='+login
		else:
			redirect_location = '/login?error=1&from='+redirect_location+'&login='+login
	else:
		redirect_location = '/login?error=1&from='+redirect_location
	redirect_location = '/home' if redirect == False else handler.path[11:]
	handler.do_GET_REDIRECT(redirect_location,headers=redirect_headers)
