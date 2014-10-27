# coding=UTF-8

@pageTemplate('VIEW-POSTS')
def template_Posts_page(url_args,user=None,session=None,**kwargs):
	yield _template_PAGEHEAD(pagetitle='ABlog - Posts')
	yield _template_NAVBAR()
	###
	yield _template_GRID_BEGIN( )
	yield _template_GRID_ROW_START( )
	#### Login form
	yield """
	<div class='col-md-3 col-lg-2'>
		<div class='panel panel-default'>
			<div class='panel-heading'>Login</div>
			<div class='panel-body'>"""
	yield _template_LOGIN_FORM( )
	yield """
			</div>
			<div class='panel-footer'></div>
		</div>
	</div>"""
	#### Posts
	yield """<div class='col-md-6 col-lg-8'>"""
	first = int(url_args.get('start',0))
	count = int(url_args.get('count',10))
	posts = makeDBRequest('GET-POSTS',first=first,count=count)
	if posts == None:
		yield """
		<p align='center' color='red'>DB Request error</p>
		"""
	else:
		for post in posts:
			yield """
				<div class='panel panel-default'>
					<div class='panel-body'>"""
			yield post['text'].replace('&','&amp').replace('<','&lt;').replace('>','&gt;')
			yield """
				</div>
				<div class='panel-footer' align='right'>"""
			### Creation time and user name
			yield str(post['ctime'])
			yield ' by '
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
