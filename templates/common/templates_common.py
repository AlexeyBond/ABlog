#!/usr/bin/python
# coding=UTF-8

def _template_PAGEHEAD(pagetitle='<DEFAULT_TITLE>',icon=None):
	yield """<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>"""
	yield pagetitle
	yield """</title>

		<!-- Bootstrap -->
		<link href="/resource/bootstrap/css/bootstrap.min.css" rel="stylesheet">

		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
		<!--[if lt IE 9]>
			<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
			<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
		<![endif]-->
	</head>
	<body>"""

def _template_PAGEFOOTER():
	return """
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js" />
		<script src="/resource/bootstrap/js/bootstrap.min.js" />
	</body>
</html>"""

def _template_GRID_BEGIN():
	return "<div class='container-fluid'>\n"

def _template_GRID_END():
	return "</div>\n"

def _template_GRID_ROW_START():
	return "<div class='row'>\n"

def _template_GRID_ROW_END():
	return "</div>\n"

def _template_GRID_COLUMN_START(width=1,offset=0):
	width=int(width)
	offset=int(offset)
	if offset == 0:
		return "<div class='col-md-%s'>"%(width)
	else:
		return "<div class='col-md-%s col-md-offset-%s'>"%(width,offset)

def _template_ALERT(text):
	return '<div class="alert alert-danger" role="alert">',text,'</div>'
