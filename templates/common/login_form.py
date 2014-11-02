#!/usr/bin/python
# coding=UTF-8

def _template_LOGIN_FORM(login=None):
	yield """
	<form name='login_form' action='/login' method='POST'>
		<div class="form-group">
			<div class="input-group">
				<input class="form-control" placeholder='Логин' type='text' name='login' """
	if login != None:
		yield """value='%s'"""%(login)
	yield """ />
			</div>
		</div>
		<div class="form-group">
			<div class="input-group">
				<input class="form-control" type='password' placeholder='Пароль' name='password' />
			</div>
		</div>
		<div class="form-group">
			<div class="input-group">
				<input type='submit' class='btn btn-xs btn-primary' value='Войти!' />
				<span width='10px' />
				<a href='/register' class='btn btn-xs btn-default'>Регистрация...</a>
			</div>
		</div>
	</form>"""

def _template_login_panel():
	yield """
		<div class='panel panel-default'>
			<div class='panel-heading'>
				Вход
			</div>
			<div class='panel-body'>"""
	yield _template_LOGIN_FORM( )
	yield """
			</div>
			<div class='panel-footer'>
			</div>
		</div>"""
