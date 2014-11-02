# coding=UTF-8


@pageTemplate('LOGIN-PAGE')
def template_login_page(url_args,**kwargs):
	yield _template_PAGEHEAD(pagetitle='ABlog - Вход')
	yield _template_NAVBAR()
	###
	yield """
	<div class='col-md-4 col-md-offset-4'>
		<div class='panel panel-default'>
			<div class='panel-heading'>Вход</div>
			<div class='panel-body'>"""
	####
	if 'error' in url_args:
		yield """
		<div class="alert alert-danger" role="alert">Неверный логин или пароль.</div>"""
	####
	if 'login' in url_args:
		yield _template_LOGIN_FORM(login=url_args['login'])
	else:
		yield _template_LOGIN_FORM( )
	####
	yield """
			</div>
			<div class='panel-footer'></div>
		</div>
	</div>"""
	###
	yield _template_PAGEFOOTER()
