# coding=UTF-8

@POSTRequestHandler('^/edit-profile')
def post__edit_profile(handler,**kwargs):
	session = makeDBRequest('IDENTIFY-USER-BY-COOKIES',cookies=handler.cookies)
	form = handler.do_POST_parse_form( )
	url_args = parseUrlParameters(handler.path)
	if 'action' not in url_args or session == None:
		handler.do_GET_404()
		return
	#
	def backToProfile():
		handler.do_GET_REDIRECT('/user?id='+str(session['user_id']))
		return
	#
	if url_args['action'] == 'avatar':
		if 'avafile' not in form:
			return backToProfile( )
		file_name = form['avafile'].filename
		file_data = form['avafile'].file.read()
		new_path = 'resource/avatar/'+str(session['user_id'])+'-'+str(time.time())+'-'+file_name
		print 'Uploading avatar file ',file_name,' for user #',session['user_id'],' to ',new_path
		ofile = open(rel2absPath(new_path),'w')
		ofile.write(file_data)
		ofile.close( )
		makeDBRequest('SET-USER-AVATAR-PATH',userid=session['user_id'],path=new_path)
		return backToProfile( )
	elif url_args['action'] == 'edit':
		user_email = form['email'].value if 'email' in form else None
		user_about = form['user_about'].value if 'user_about' in form else None
		makeDBRequest('SET-USER-DATA',userid=session['user_id'],email=user_email,about=user_about)
		return backToProfile( )
	else:
		return handler.do_GET_404( )
