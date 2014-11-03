# coding=UTF-8

def _template_user_panel(user_name,user_id):
	yield """
		<div class='panel panel-default'>
			<div class='panel-heading'>
				<a href='/user?id=""",str(user_id),"""'><span class="glyphicon glyphicon-user" />"""
	yield user_name
	yield """</a>
			</div>
			<div class='panel-body'>
				<a href='/logout' class='btn btn-xs btn-default'>Выйти</a>
				<a href='/new' class='btn btn-xs btn-primary'>Новая запись...</a>
			</div>
		</div>"""

def _template_user_panel_or_login_panel(session):
	if session != None:
		return _template_user_panel(
			user_name=session['user_name'],
			user_id=session['user_id'])
	else:
		return _template_login_panel()
