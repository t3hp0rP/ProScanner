import requests
import threadpool
import Queue
import sys
import os
from prettytable import PrettyTable

#init
class Core(object):
	"""
		core class for scanner
		init_arg :
			url --- url to scan
			threadNum --- threadNum (Default 5)
			cookie --- cookie use for requests
			retry --- retry times
	"""

	def __init__(self, url, threadNum = 50, cookie = {}, retry=10):
		super(Core, self).__init__()
		self.__url = url
		self.__threadNum = threadNum
		self.__cookie = cookie
		self.__session = requests.Session()
		self.__retry = retry
		self.result_success = []
		self.result_fail = []
		self.prettytable = PrettyTable(['url','statusCode'])

	def patchVar(self):
		#read dictionary
		try:
			dic1 = open(sys.path[0]+'/core/list.txt','rb')
			dic2 = open(sys.path[0]+'/core/file.txt','rb')

			src = []
			for x in dic1:
				src.append(x.strip())
			for x in dic2:
				src.append(x.strip())
			num = len(src)
			func_var = []
			for x in xrange(1,num/20+1):
				lst = []
				queue = Queue.Queue(0)
				for line1 in src[x*20:x*20+20]:
					# lst.append(line1.strip())
					queue.put([line1.strip(),0])
				func_var.append(queue)

			return func_var
		except Exception as e:
			raise e

	def createThread(self):
		pool = threadpool.ThreadPool(self.__threadNum)
		func_var = self.patchVar()
		tasks = threadpool.makeRequests(self.req,func_var)
		[pool.putRequest(task) for task in tasks]
		pool.wait()

	def req(self,queue):
		while not queue.empty():
			url = queue.get()
			# print '[*] trying ' + self.__url+'/'+url[0]
			sys.stdout.write('[*] trying ' + self.__url+url[0] + '\n')
			sys.stdout.flush()
			try:
				res = self.__session.get(self.__url+url[0],cookies=self.__cookie,timeout=10)
				if (str(res.status_code)[0] in ['1','2','3','4']) and (res.status_code != 404):
					self.result_success.append([url[0],res.status_code])
			except Exception as e:
				if url[1] >= self.__retry:
					queue.put([url[0],url[1]+1])
				else:
					self.result_fail.append(url[0])

	def getRes(self):
		self.prettytable.align['url'] = 1
		self.prettytable.padding_width = 1
		self.result_success = sorted(self.result_success,key=lambda x: x[1])
		for s in self.result_success:
			self.prettytable.add_row([s[0],s[1]])
		for f in self.result_fail:
			self.prettytable.add_row([f,'failToRequest'])
		print self.prettytable