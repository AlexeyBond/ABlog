# coding=UTF-8


@pageTemplate('HOMEPAGE')
def template_Homepage(user=None,session=None,**kwargs):
	yield _template_PAGEHEAD(pagetitle='ABlog - Home')
	yield _template_NAVBAR()
	###
	yield _template_GRID_BEGIN( )
	yield _template_GRID_ROW_START( )
	####
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
	####
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
