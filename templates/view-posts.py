# coding=UTF-8

@pageTemplate('VIEW-POSTS')
def template_Posts_page(url_args,session=None,**kwargs):
	### Make DB requests ...
	session_user = session['user_id'] if session != None else None
	first = int(url_args.get('start',0))
	count = int(url_args.get('count',10))
	userid = url_args.get('user',None)
	if userid != None:
		userid = int(userid)
	page_title = 'ABlog - Записи'
	if userid == session_user and userid != None:
		page_title = 'ABlog - Мои записи'
	elif userid != None:
		uname = makeDBRequest('GET-USER-NAME',userid=userid)
		if uname != None:
			page_title = page_title + ' пользователя ' + uname
		else:
			userid = None
	posts = makeDBRequest('GET-POSTS',first=first,count=count,user_id=userid)
	###
	yield _template_PAGEHEAD(pagetitle=page_title)
	yield _template_NAVBAR()
	###
	yield _template_GRID_BEGIN( )
	yield _template_GRID_ROW_START( )
	#### Login form or user panel
	yield """
	<div class='col-md-3 col-lg-2'>"""
	yield _template_user_panel_or_login_panel(session=session)
	yield """
	</div>"""
	#### Posts
	yield """<div class='col-md-6 col-lg-8'>"""
	if posts == None:
		yield """
		<p align='center' color='red'>Ошибка обращения к базе данных</p>
		"""
	else:
		for post in posts:
			yield """
				<div class='panel panel-default'>"""
			if post['uid'] == session_user:
				yield """
					<div class='panel-heading'>
						<a class='btn btn-default btn-xs' href='/delete?post="""
				yield str(post['post_id'])
				yield """'>Удалить</a>
						<a class='btn btn-default btn-xs' href='/edit?post="""
				yield str(post['post_id'])
				yield """'>Редактировать...</a>
					</div>"""
			yield """
					<div class='panel-body'>"""
			yield post['text'].replace('&','&amp').replace('<','&lt;').replace('>','&gt;')
			yield """
				</div>
				<div class='panel-footer' align='right'>"""
			### Creation time and user name
			yield 'Написано '
			yield str(post['ctime'])
			yield ' пользователем '
			yield '<a href="/user?id='
			yield str(post['uid'])
			yield '">@'
			yield post['user']
			yield '</a>'
			###
			yield """</div></div>"""
	yield """</div>"""
	#### Users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
