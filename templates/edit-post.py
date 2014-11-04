# coding=UTF-8

@pageTemplate('EDIT-POST')
def template_edit_post(handler,session,url_args,**kwargs):
	session_user = session['user_id'] if session != None else None
	post_id = url_args.get('id',None)
	post = None
	error = False
	if post_id == None or session_user == None:
		error = True
	else:
		post_id = int(post_id)
		post = makeDBRequest('GET-POST',post_id=post_id)
		if post == None:
			error = True
		else:
			if post['uid'] != session_user:
				error = True
	#
	yield _template_PAGEHEAD(pagetitle='ABlog - Редактирование записи')
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
				Редактирование записи
			</div>
			<div class='panel-body'>
				<form name='post_edit_form' action='/edit-post?id=%s' method='POST'>"""%(post_id)
		yield """
					<div class="form-group">
						<label class='control-label' for='input-text'>Текст записи</label>
						<textarea class='form-control' style='resize:none' rows='3' maxlength='255' wrap='soft' name='post_text' id='input-about'>%s</textarea>
					</div>"""%(post['text'])
		yield """
					<div class="form-group">
						<div class="input-group">
							<input type='submit' class='btn btn-xs btn-primary' value='Сохранить!' />
						</div>
					</div>
				</form>
			</div></div>"""
	yield """</div>"""
	#### Users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()