# coding=UTF-8


@pageTemplate('NEW-POST')
def template_Homepage(session=None,**kwargs):
	yield _template_PAGEHEAD(pagetitle='ABlog - Новая запись')
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
	#### 2'nd column - post panel
	yield """
	<div class='col-md-6 col-lg-8'>
		<div class='panel panel-default'>
			<div class='panel-heading'>
				Новая запись
			</div>
			<div class='panel-body'>
				<form name='post_form' action='/new' method='POST'>"""
	if session == None:
		yield """
					<div class='form-group'>
						<input type='text' name='login' placeholder='Логин' class='form-control' />
					</div>
					<div class='form-group'>
						<input type='password' name='password' placeholder='Пароль' class='form-control' />
					</div>"""
	yield """
					<div class="form-group">
							<textarea class='form-control' style='resize:none' rows='3' maxlength='255' autofocus wrap='soft' name='post_text'></textarea>
					</div>
					<div class="form-group">
						<div class="input-group">
							<input type='submit' class='btn btn-xs btn-primary' value='Отправить!' />
						</div>
					</div>
				</form>
			</div>
		</div>"""
	yield """
	</div>"""
	#### 3'rd column - users list
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
