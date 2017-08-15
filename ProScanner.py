from core.core import Core
import time
import sys
import getopt

def usage():
	print '''
	-h or --help : For help
	-u or --url : The url you want to scan
	-t or --thread_num : The thread number you want to set, Default 50
	-c or --cookie : The cookie you want to use, Default Null
	-r or --retry : Retry times, Default 10
	
	Eg : python Pscanner.py -u localhost -t 30 -c 'user=admin;pass=123' -r 5

	ONLY FOR CTF Competition
	'''

def serializeCookie(raw):
	lis = raw.slpit(';')
	lis = filter(lambda x: x!='' ,lis)
	dic = {}
	for x in lis:
		a,b = x.slpit('=')
		dic[a] = b
	return dic

def main():
	url = ''
	t = 30
	r = 10
	c = ''
	try:
		opt,argv = getopt.getopt(sys.argv[1:],'hu:t:',['help','url'])
		if opt == []:
			print '\t[!] Please input the parameter.'
			usage()
			exit()
	except getopt.GetoptError as e:
		print e
		usage()
		exit(0)
	for o,v in opt:
		if o in ('-h','--help'):
			usage()
			exit(0)
		if o in ('-u','--url'):
			if v == '':
				print 'url can\'t be null'
				exit(0)
			url.strip()
			if v[0:7] != 'http://':
				v = 'http://' + v
			if v[-1] != '/':
				v += '/'
			url = v
		if o in ('-t','--thread_num'):
			if v.isdigit():
				thread_num = int(v)
			else :
			 	print 'Thread_num is NOT a digit!'
			 	exit(0)	
		if o in ('-c','--cookie'):
			c = serializeCookie(v)
		if o in ('-r','--retry'):
			if v.isdigit():
				retry = int(v)
			else :
			 	print 'retry times is NOT a digit!'
			 	exit(0)	
	print '[*] Start'
	sTime = time.time()
	# print str(sTime)
	a = Core(url,t,c,r)
	a.createThread()
	a.getRes()
	print '[*] End ------'
	print '[*] Used ' + str(time.time()-sTime)

if __name__ == '__main__':
	main()
