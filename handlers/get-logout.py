# coding=UTF-8


@GETRequestHandler('^/logout')
def get__logout(handler,**kwargs):
	url_args = parseUrlParameters(handler.path)
	redirect_location = url_args['from'] if 'from' in url_args else '/home'
	headers = [
		('Set-Cookie','sessionid=; expires=Thu, 01 Jan 1970 00:00:00 GMT')]
	handler.do_GET_REDIRECT(location=redirect_location,headers=headers)

