# coding=UTF-8


@POSTRequestHandler('^/edit-post')
def post__edit_post(handler,**kwargs):
	session = makeDBRequest('IDENTIFY-USER-BY-COOKIES',cookies=handler.cookies)
	form = handler.do_POST_parse_form( )
	url_args = parseUrlParameters(handler.path)
	if session == None:
		return handler.do_GET_404()
	if 'id' not in url_args:
		return handler.do_GET_404()
	post = makeDBRequest('GET-POST',post_id=url_args['id'])
	if post == None:
		return handler.do_GET_404()
	if post['uid'] != session['user_id']:
		return handler.do_GET_404()
	new_text = form['post_text'].value if 'post_text' in form else ''
	makeDBRequest('MODIFY-POST',post_id=int(url_args['id']),new_text=new_text)
	handler.do_GET_REDIRECT('/posts')
