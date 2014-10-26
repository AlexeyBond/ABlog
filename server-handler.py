# coding=UTF-8
import re
import cgi

class myHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def send_headers(self,headers):
		if headers != None:
			for k, v in headers.items():
				self.send_header(k,v)

	def do_GET_REDIRECT(self,location,headers=None):
		self.send_response(303)
		self.send_headers(headers)
		self.send_header('Location',location)

	def do_POST_parse_form(self):
		form = cgi.FieldStorage(
			fp=self.rfile, 
			headers=self.headers,
			environ={'REQUEST_METHOD':'POST',
					'CONTENT_TYPE':self.headers['Content-Type'],
		})
		return form

	def start_response(self,code=200,content_type='text/html',charset=None,headers=None):
		global SERVER_TITLE
		# Send response code
		self.send_response(code)
		# Say who we are
		self.send_header('Server',SERVER_TITLE)
		# Send Content-Type header
		if content_type != None:
			if content_type.startswith('text/'):
				self.send_header('Content-type','%s; charset="%s"'
					%(content_type,'UTF-8' if charset == None else charset))
			else:
				self.send_header('Content-type', content_type)
		# Send other headers
		self.send_headers(headers)
		# Send CRLF
		self.end_headers( )
	def do_GET_404(self):
		self.start_response(404)
		renderPageTemplate('ERROR_404',self.wfile)
	def do_GET(self):
		hfunc = selectPathHandler(self.path,REQUEST_HANDLERS_GET)
		if hfunc != None:
			hfunc(handler=self)
		else:
			self.do_GET_404( )
	def do_POST(self):
		hfunc = selectPathHandler(self.path,REQUEST_HANDLERS_POST)
		if hfunc != None:
			hfunc(handler=self)
		else:
			self.do_GET_404( )


REQUEST_HANDLERS_DIR_NAME = 'handlers'

REQUEST_HANDLER_CLASS = myHandler

REQUEST_HANDLERS_DIR_PATH = rel2absPath(REQUEST_HANDLERS_DIR_NAME)

REQUEST_HANDLERS_GET = []
REQUEST_HANDLERS_POST = []

def RequestHandlerDecorator(reqname):
	def x_requestHandler(pathexpr,**decKWargs):
		def decorator(func):
			def wrapper(**kwargs):
				fullkwargs = dict(decKWargs.items()+kwargs.items())
				return func(**fullkwargs)
			globals()['REQUEST_HANDLERS_'+reqname].append((re.compile(pathexpr),wrapper))
			print 'New handler for %s requests with url %s'%(reqname,pathexpr)
			return func
		return decorator
	return x_requestHandler

POSTRequestHandler = RequestHandlerDecorator('POST')
GETRequestHandler = RequestHandlerDecorator('GET')

def selectPathHandler(path,hlist):
	for p in hlist:
		if p[0].search(path) != None:
			return p[1];
	return None

def loadRequestHandlers():
	# global REQUEST_HANDLERS_DIR_PATH
	# filelist = os.listdir(REQUEST_HANDLERS_DIR_PATH)
	global REQUEST_HANDLERS_DIR_NAME
	print '---   Loading request handlers   ---'
	loadFiles(relative=REQUEST_HANDLERS_DIR_NAME)
	# for fn in filelist:
	# 	if fn.endswith('.py'):
	# 		loadFile(os.path.join(REQUEST_HANDLERS_DIR_PATH,fn))
	print '--- End loading request handlers ---'

loadRequestHandlers( )
