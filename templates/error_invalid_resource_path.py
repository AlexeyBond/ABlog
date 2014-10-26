# coding=UTF-8

@pageTemplate('ERROR_BAD_RESOURCE_PATH')
def template_error_bad_resource_path(**kwargs):
	yield _template_PAGEHEAD(pagetitle='Bad resource path.')
	yield """
	<span align='center'>
		<h1>Bad resource file path !!!</h1>
	</span>
	<span align='right'>
		<p>Did not you try to crack this site?</p>
	</span>"""
	yield _template_PAGEFOOTER()
