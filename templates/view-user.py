# coding=UTF-8

DEFAULT_USER_AVATAR_PATH = '/resource/avatar/default.gif'

@pageTemplate('VIEW-USER')
def template_view_user(session,url_args,**kwargs):
	global DEFAULT_USER_AVATAR_PATH
	userid = url_args.get('id',None)
	session_user = session['user_id'] if session != None else None
	my_profile = False
	avapath = DEFAULT_USER_AVATAR_PATH
	error = False
	udata = None
	pagetitle = ''
	user_posts = None
	if userid == None:
		error = True
	else:
		userid = int(userid)
		my_profile = (session_user == userid and userid != None)
		udata = makeDBRequest('GET-USER-INFO',userid=userid)
		if udata == None:
			error = True
		else:
			if my_profile:
				pagetitle = 'ABlog - Мой профиль'
			else:
				pagetitle = 'ABlog - Профиль пользователя ' + udata['name']
			if udata['avapath'] != None:
				avapath = udata['avapath']
			user_posts = makeDBRequest('GET-POSTS-COUNT',user_id=userid)
	###
	yield _template_PAGEHEAD(pagetitle=pagetitle)
	yield _template_NAVBAR()
	###
	yield _template_GRID_BEGIN( )
	yield _template_GRID_ROW_START( )
	#### 1'st column - user/login panel
	yield """
	<div class='col-md-3 col-lg-2'>"""
	yield _template_user_panel_or_login_panel(session)
	yield """
	</div>"""
	#### 
	yield """<div class='col-md-6 col-lg-8'>"""
	if error:
		yield """<div class="alert alert-danger" role="alert">Ошибка</p>"""
	else:
		yield """
			<div class='row'>"""
		yield """
				<div class='col-md-4'>
					<a href='""",avapath,"""'>
						<img class='img-circle img-thumbnail' src='""",avapath,"""'></img>
					</a>
				</div>"""
		yield """
				<div class='col-md-8'>"""
		yield """<h3 class='media-heading'>""",udata['name']
		yield """ <small>(записей: <a href='/posts?user=""",str(userid),"""'>""",user_posts,"""</a>)</small></h3>"""
		if udata['email'] != None:
			yield """<p>e-mail: <a href='mailto:""",udata['email'],"'>",udata['email'],"</a><p>"
		else:
			yield """<p>e-mail: Не указан</p>"""
		##
		yield '<p>',udata['name'],' о себе'
		if udata['about'] == None:
			yield ' ничего не рассеазывает.'
		else:
			yield ': ',udata['about'].replace('&','&amp;').replace('<','&lt;').replace('>','&gt')
		yield '</p>'
		##
		if my_profile:
			yield """
					<a class='btn btn-default' href='/edit-profile'>
						<span class='glyphicon glyphicon-pencil' />
						Редактировать...
					</a>"""
		yield """
				</div>
			</div>"""
	yield """</div>"""
	#### Users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
