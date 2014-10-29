# coding=UTF-8


@pageTemplate('ABOUTPAGE')
def template_About(**kwargs):
	yield _template_PAGEHEAD(pagetitle='ABlog - О сайте')
	yield _template_NAVBAR()
	###
	yield FILE_CACHE.getFile(rel2absPath('resource/about.part.html'))[0]
	###
	yield _template_PAGEFOOTER()
