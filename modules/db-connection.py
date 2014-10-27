# coding=UTF-8
import MySQLdb
import json
import time

class DatabaseConnection:
	# 
	def _make_request(self,requeststr,select_map=None,**kwargs):
		if self.connected == False:
			print '!!! DB %s@%s not connected. Trying to connect again.'%(
				self.db_name,self.db_host)
			self.connect( )
			if self.connected == False:
				print '!!! Request failed'
				return None
		requeststr = requeststr.format(
			db_name=self.db_name,
			**kwargs)
		try:
			cursor = self.connection.cursor()
			cursor.execute(requeststr)
			result = cursor.fetchall()
			cursor.close( )
		except Exception as e:
			print '!!! Request failed with exception:\n',e
			return None
		if select_map != None:
			final_result = []
			for row in result:
				dct = dict(zip(select_map,row))
				final_result.append(dct)
			return final_result
		return result

	# 
	def commit(self):
		self.connection.commit( )

	# 
	def connect(self):
		try:
			self.connection = MySQLdb.connect(
					host=self.db_host,
					user=self.db_user_name,
					passwd=self.db_user_passwd,
					db=self.db_name
				)
			print 'Connected to db %s@%s as %s' %(
				self.db_name,self.db_host,self.db_user_name)
			self.connected = True
		except Exception as e:
			print '!!! Exception while connecting to DB %s@%s'%(
				self.db_name,self.db_host)
			print e
	#
	def close(self):
		self.connection.commit( )
		self.connection.close( )
	#
	def configure(self,config):
		self.db_name = config['BASE_NAME']
		self.db_host = config['HOST']
		self.db_user_name = config['USER_NAME']
		self.db_user_passwd = config['USER_PASSWD']
	# 
	def __init__(self,conf):
		self.connected = False

		self.configure(conf)
		self.connect( )

		self.top20_users = None
		self.top20_users_utime = 0

DB_CONFIG_PATH = 'config/db.cfg'
DB_REQUEST_HANDLERS_DIR = 'db-requests'

DB_REQUEST_HANDLERS = {}
DB_CONNECTIONS = {}

def dbRequestHandler(db_name,request_name):
	def dbRequestDecorator(func):
		print 'Loaded handler for request %s to base %s'%(
			request_name,db_name)
		def dbRequestWrapper(**kwargs):
			if db_name not in DB_CONNECTIONS:
				print '!!! Database connection %s for request %s not found'%(
					db_name,request_name)
				return None
			db = DB_CONNECTIONS[db_name]
			return func(db=db,**kwargs)
		DB_REQUEST_HANDLERS[request_name] = dbRequestWrapper
		return func
	return dbRequestDecorator

def makeDBRequest(request_name,**kwargs):
	if request_name not in DB_REQUEST_HANDLERS:
		print '!!! DB request %s not found'%(request_name)
		return None
	return DB_REQUEST_HANDLERS[request_name](**kwargs)

# Stores result of function call for <seconds>
# !WARNING!
# Doesn't care if function is called with other arguments
def storeResult(seconds):
	def storeResultDecorator(func):
		resultStorage = {'result':None,'time':0}
		def storeResultWrapper(*args,**kwargs):
			ctime = time.time( )
			if (resultStorage['result'] == None or
				ctime > (resultStorage['time']+seconds) ):
				resultStorage['result'] = func(*args,**kwargs)
				resultStorage['time'] = ctime
			return resultStorage['result']
		return storeResultWrapper
	return storeResultDecorator

loadModuleGroup('DB-REQUEST-HANDLERS',DB_REQUEST_HANDLERS_DIR)

#
def initDBConnections( ):
	global DB_CONFIG_PATH
	global DB_CONNECTIONS
	conf = json.load(open(rel2absPath(DB_CONFIG_PATH),'r'))
	for k,v in conf.items():
		DB_CONNECTIONS[k] = DatabaseConnection(v)
		print 'Initialized DB connection ',k

#
@callOnShutdown
def closeDBConnections( ):
	global DB_CONNECTIONS
	for name,conn in DB_CONNECTIONS.items():
		try:
			if conn.connected != False:
				conn.close( )
		except Exception as e:
			print '!!! Exception while closing connection to DB ',name
			print e


initDBConnections( )
