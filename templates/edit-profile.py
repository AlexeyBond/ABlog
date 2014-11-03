# coding=UTF-8


@pageTemplate('EDIT-PROFILE')
def template_edit_profile(session,**kwargs):
	session_user = session['user_id'] if session != None else None
	error = False
	if session_user == None:
		error = True
	else:
		session_user = int(session_user)
		udata = makeDBRequest('GET-USER-INFO',userid=session_user)
		if udata == None:
			error = True
	###
	yield _template_PAGEHEAD(pagetitle='ABlog - Редактирование профиля')
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
	if error == True:
		yield _template_ALERT('Ошибка.')
	else:
		yield """
		<div class='panel panel-default'>
			<div class='panel-heading'>
				Редактирование профиля
			</div>
			<div class='panel-body'>
				<form name='profile_edit_form' action='/edit-profile?action=edit' method='POST'>"""
		yield """
					<div class='form-group'>
						<label class='control-label' for='input-email'>e-mail:</label>
						<input type='text' name='email' placeholder='e-mail' class='form-control' id='input-email' value='%s' />
					</div>"""%(udata['email'] or '')
		yield """
					<div class="form-group">
						<label class='control-label' for='input-about'>Расскажите о себе</label>
						<textarea class='form-control' style='resize:none' rows='3' maxlength='255' wrap='soft' name='user_about' id='input-about'>%s</textarea>
					</div>"""%(udata['about'] or '')
		yield """
					<div class="form-group">
						<div class="input-group">
							<input type='submit' class='btn btn-xs btn-primary' value='Сохранить!' />
						</div>
					</div>
				</form>"""
		yield """
				<form  enctype="multipart/form-data" name='avatar_upload_form' action='/edit-profile?action=avatar' method='POST'>
					<div class='form-group'>
						<label class='control-label' for='input-ava'>Поменять аватар...</label>
						<input type='file' name='avafile' class='form-control' id='input-ava' />
					</div>
					<div class='form-group'>
						<input type='submit' class='btn btn-xs btn-primary' value='Отправить!' />
					</div>
				</form>"""
		yield """
			</div></div>"""
	yield """</div>"""
	#### Users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
