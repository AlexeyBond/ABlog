# coding=UTF-8

@pageTemplate('VIEW-USERS')
def template_Users_page(url_args,session=None,**kwargs):
	first = int(url_args.get('start',0))
	count = int(url_args.get('count',10))
	error = False
	if first < 0:
		first = 0
	users = makeDBRequest('GET-USERS',first=first,count=count);
	total = makeDBRequest('GET-USERS-COUNT')
	if users == None or total == None:
		error = True
	###
	yield _template_PAGEHEAD(pagetitle='ABlog - Пользователи')
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
	#### Users
	yield """<div class='col-md-6 col-lg-8'>"""
	if error:
		yield _template_ALERT('Ошибка обращения к базе данных.')
	else:
		def pageswitch():
			yield """
					<div class='text-center'>
					<div class='btn-group'>
						<a class='btn btn-default' href='/users?start=0&count=""",str(count),"""'>
							<span class="glyphicon glyphicon-fast-backward"></span>
						</a>
						<a class='btn btn-default' """
			if first <= 0:
				yield "disabled='disabled'"
			else:
				yield "href='/users?start=",str(first-count),"&count=",str(count),"'"
			yield """>
							<span class="glyphicon glyphicon-backward"></span>
						</a>
						<a class='btn btn-default' href='#'>
							""",str(first+1),'..',str(first+count),"""
						</a>
						<a class='btn btn-default' """
			if first+count >= total:
				yield "disabled='disabled'"
			else:
				yield "href='/users?start=",str(first+count),"&count=",str(count),"'"
			yield """>
							<span class="glyphicon glyphicon-forward" ></span>
						</a>
						<a class='btn btn-default' """
			if count >= total:
				yield "disabled='disabled'"
			else:
				yield "href='/users?start=",str(total-count),"&count=",str(count),"'"
			yield """>
							<span class="glyphicon glyphicon-fast-forward"></span>
						</a>
					</div>
					</div><br/>"""
		yield pageswitch( )
		yield """
		<div class="list-group">"""
		for user in users:
			yield """
			<div class="list-group-item">
				<p class='list-group-item-text'><a href='/user?id=""",user['id'],"""'>"""
			yield user['name']
			yield """
				</a></p>
			</div>"""
		yield """
		</div>"""
		yield pageswitch( )
	yield """</div>"""
	#### Users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
