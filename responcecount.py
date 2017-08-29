import urllib2
import sys

############define variables######
res=0
thread=0

vmval=open('vmmin.txt','r+')
for i in vmval:
	vmmin=int(i)

vmmax=30
##########code block############
uiaas = open('uiaas_servers.txt','r+')	
for host in uiaas:
	hosts=host.rstrip("\n")	
	responce=urllib2.urlopen('http://{}:8080/monitoring?part=lastValue&graph=usedhttpMeanTimes'.format(hosts)).read()
	threads=urllib2.urlopen('http://{}:8080/monitoring?part=lastValue&graph=activeThreads'.format(hosts)).read()
	#print responce,threads
	res += float(responce)
	thread += float(threads)
print res,thread

if (thread > 300 and res > 40):
	print "working"
	
	if (vmmin < vmmax):
		print "create new vm"
		vmmin += int(1)
		print vmmin
		vmval.seek(0)
		vmval.truncate()
		vmval.write(str(vmmin))

	else:
		print "out of capacity"
	
else:
	sys.exit()

vmval.close()

	




