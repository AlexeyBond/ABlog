# coding=UTF-8


@pageTemplate('REGISTER-PAGE')
def template_register_page(url_args,session=None,**kwargs):
	login_val = url_args.get('login','')
	login_incorrect_error = 'login_incorrect' in url_args
	login_in_use_error = 'login_in_use' in url_args
	password_incorrect_error = 'password_incorrect' in url_args
	password_mismatch_error = 'password_mismatch' in url_args

	###
	yield _template_PAGEHEAD(pagetitle='ABlog - Регистрация')
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
	#### 2'nd column - registration form
	yield """
	<div class='col-md-6 col-lg-8'>
		<div class='panel panel-default'>
			<div class='panel-heading'>
				Регистрация
			</div>
			<div class='panel-body'>
				<form name='register_form' action='/register' method='POST'>"""
	##### Login field
	if login_incorrect_error:
		yield """
					<div class='form-group has-error has-feedback'>
						<label class='control-label' for='input-login'>Недопустимый логин. Введите допустимый логин.</label>
						<input type='text' name='login' placeholder='Логин' class='form-control' id='input-login' />
						<span class="glyphicon glyphicon-remove form-control-feedback"></span>
					</div>"""
	elif login_in_use_error:
		yield """
					<div class='form-group has-error has-feedback'>
						<label class='control-label' for='input-login'>Этот логин уже используется. Введите какой-нибудь другой.</label>
						<input type='text' name='login' placeholder='Логин' class='form-control' id='input-login' value='%s' />
						<span class="glyphicon glyphicon-remove form-control-feedback"></span>
					</div>"""%(login_val)
	else:
		yield """
					<div class='form-group'>
						<label class='control-label' for='input-login'>Выбирете логин, соответствующий регулярному выражению %s </label>
						<input type='text' name='login' placeholder='Логин' class='form-control' id='input-login' value='%s' />
					</div>"""%(REGEXP_VALID_LOGIN.pattern,login_val)
	##### Password fields
	if password_incorrect_error or password_mismatch_error:
		yield """
					<div class='form-group has-error has-feedback'>
						<label class='control-label' for='input-password-1'>Выбирете пароль, соответствующий регулярному выражению %s </label>
						<input type='password' name='password' placeholder='Пароль' class='form-control' id='input-password-1' />
						<span class="glyphicon glyphicon-remove form-control-feedback"></span>
					</div>
					<div class='form-group has-error has-feedback'>
						<label class='control-label' for='input-password-2'>Повторите пароль</label>
						<input type='password' name='password_repeat' placeholder='Повторите пароль' class='form-control' id='input-password-2' />
						<span class="glyphicon glyphicon-remove form-control-feedback"></span>
					</div>"""%(REGEXP_VALID_PASSWORD.pattern)
	else:
		yield """
					<div class='form-group'>
						<label class='control-label' for='input-password-1'>Выбирете пароль, соответствующий регулярному выражению %s </label>
						<input type='password' name='password' placeholder='Пароль' class='form-control' id='input-password-1' />
					</div>
					<div class='form-group'>
						<label class='control-label' for='input-password-2'>Повторите пароль</label>
						<input type='password' name='password_repeat' placeholder='Повторите пароль' class='form-control' id='input-password-2' />
					</div>"""%(REGEXP_VALID_PASSWORD.pattern)
	##### 
	yield """
					<div class="form-group">
						<div class="input-group">
							<input type='submit' class='btn btn-xs btn-primary' value='Зарегистрироваться!' />
						</div>
					</div>
				</form>
	</div></div></div>"""
	#### 3'rd column - users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
