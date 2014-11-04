# coding=UTF-8


@pageTemplate('HOMEPAGE')
def template_Homepage(session=None,**kwargs):
	yield _template_PAGEHEAD(pagetitle='ABlog')
	yield _template_NAVBAR()
	###
	yield _template_GRID_BEGIN( )
	yield _template_GRID_ROW_START( )
	####
	yield """
	<div class='col-md-3 col-lg-2 col-md-offset-3 col-lg-offset-4'>"""
	yield _template_user_panel_or_login_panel(session)
	yield """
	</div>"""
	####
	yield _template_user_list_table()
	####
	yield _template_GRID_ROW_END( )
	yield _template_GRID_END( )
	###
	yield _template_PAGEFOOTER()
