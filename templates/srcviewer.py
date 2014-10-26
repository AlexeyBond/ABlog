# coding=UTF-8

@pageTemplate('SRCVIEW_ROOT')
def template_srcview_root(**kwargs):
	return """<!DOCTYPE html>
	<html>
		<head>
			<title>Source view</title>
		</head>
		<frameset rows='*' cols='20%,*'>
			<frame name='SRCVIEW_FRAME_TREEVIEW' src='/src/tree' />
			<frame name='SRCVIEW_FRAME_CODEVIEW' src='/resource/srcview-about.html' />
		</frameset>
	</html>"""

@pageTemplate('SRCVIEW_TREE')
def template_srcview_root(**kwargs):
	yield _template_PAGEHEAD(pagetitle='')
	###
	yield """
	<span class="glyphicon glyphicon-folder-open" /> /src
	<ul>"""
	flist = os.listdir(rel2absPath('.'))
	for x in flist:
		if x.endswith('.py'):
			yield """<li><a href='/src/view?file="""
			yield x
			yield """' target='SRCVIEW_FRAME_CODEVIEW'>  """
			yield x
			yield """</a></li>"""
	yield """</ul>"""
	yield """<p><a href='/resource/srcview-about.html' target='SRCVIEW_FRAME_CODEVIEW'>[about]</a></p>"""
	###
	yield _template_PAGEFOOTER()

@pageTemplate('SRCVIEW_FILE')
def template_srcview_file(url_args,**kwargs):
	global RESOURCE_PATH_VALIDATION_EXPRESSION # From /handlers/get-resource.py
	file_data = 'No file selected'
	if 'file' in url_args:
		fpath = url_args['file']
		if (RESOURCE_PATH_VALIDATION_EXPRESSION.search(fpath) == None and
			fpath.endswith('.py') ):
			file_data = (FILE_CACHE.getFile(url_args['file'])[0]
				.replace('&','&amp;')
				.replace('<','&lt;')
				.replace('>','&gt;'))
	yield _template_PAGEHEAD(pagetitle='')
	###
	yield """<pre>"""
	yield file_data
	yield """</pre>"""
	###
	yield _template_PAGEFOOTER()
