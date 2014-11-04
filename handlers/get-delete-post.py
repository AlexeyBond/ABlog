# coding=UTF-8


@GETRequestHandler('^/delete-post\\?')
def get__logout(handler,**kwargs):
	url_args = parseUrlParameters(handler.path)
	session = makeDBRequest('IDENTIFY-USER-BY-COOKIES',cookies=handler.cookies)
	if session == None:
		return handler.do_GET_404()
	if 'id' not in url_args:
		return handler.do_GET_404()
	post = makeDBRequest('GET-POST',post_id=url_args['id'])
	if post == None:
		return handler.do_GET_404()
	if post['uid'] != session['user_id']:
		return handler.do_GET_404()
	makeDBRequest('DELETE-POST',post_id=url_args['id'])
	handler.do_GET_REDIRECT('/posts')
