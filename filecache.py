# coding=UTF-8
import os

class FileCache:
	def reset(self):
		self._cached_data = {}
	def __init__(self):
		self.reset( )
	def getFile(self,filepath):
		if filepath in self._cached_data:
			record = self._cached_data[filepath]
			try:
				newmtime = os.path.getmtime(filepath)
				if record['mtime'] != newmtime:
					print 'Recaching file %s'%(filepath)
					fobj = open(filepath,'r')
					fdata = fobj.read()
					fobj.close()
					record['data'] = fdata
					record['mtime'] = newmtime
				else:
					print 'File %s in cache.'%(filepath)
			except:
				print '!!! Exception while refreshing cached file %s'%(filepath)
			return record['data'],record['mime']
		else:
			record = {}
			print 'File %s not in cache.'%(filepath)
			try:
				record['mtime'] = os.path.getmtime(filepath)
				fobj = open(filepath,'r')
				record['data'] = fobj.read()
				fobj.close()
			except Exception as e:
				print '!!! Exception while reading file to cache %s'%(filepath)
				print e
				return None,None
			record['mime'] = mimetypes.guess_type(filepath)
			self._cached_data[filepath] = record
			return record['data'],record['mime']

FILE_CACHE = FileCache( )
