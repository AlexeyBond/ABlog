#!/usr/bin/python
# coding=UTF-8

# TODO: Make more creative 404 page.
@pageTemplate('ERROR_404')
def template_error_404(**kwargs):
	yield _template_PAGEHEAD(pagetitle='404 Not found')
	yield """
	<span align='center'>
		<h1>404</h1>
		<h1>Not found !</h1>
	</span>"""
	yield _template_PAGEFOOTER()
