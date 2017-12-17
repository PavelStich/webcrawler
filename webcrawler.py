import sys
import re
import urllib2
import socket
import HTMLParser
import getopt
from threading import Thread

# Get tips
def usage():
    print('TIPS:')
    print('python pymaildumper.py [URL]')
    print('\nExample: $ python www.rada-poltava.gov.ua\n')
    return
	# Get mails
def getresult1(site, dork):

	mails = []
	for i in range(1):
	    url = 'https://www.google.com.ph/search?q=%s&start%d=&num=100&saN=&filter=0&sitesearch=%s' %(dork,i,site)
	    opener = urllib2.build_opener()
	    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	    data = opener.open(url).read() 

	    matches1 = re.findall(r'[\w\.-]+@\w+.\w+', data)

	    t1 = Thread(target=printMails,args=(matches1,))
	    t1.start()

	return mails
#Get url
def getresult2(site, dork):

	url_ad = []
	for i in range(1):
	    url = 'https://www.google.com.ph/search?q=%s&start%d=&num=100&saN=&filter=0&sitesearch=%s' %(dork,i,site)
	    opener = urllib2.build_opener()
	    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	    data = opener.open(url).read()

	    matches2 = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
	    t2 = Thread(target=printMails,args=(matches2,))
	    t2.start()


	return url_ad

#print result
def printMails(matches):
	for match in set(matches):
		print(match)


#start  searching for emails
def start1(site, dork):
	results = getresult1(site, dork)

#start  searching for pages
def start2(site, dork):
	results2 = getresult2(site, dork)

if __name__ == '__main__':
	# read args
   if len(sys.argv) == 2:
   		site = str(sys.argv[1])
   		dork = '@gmail.com'
		# start threads
   		thread1 = Thread(target=start1,args=(site, dork))
		print ('*****************')
		print('MAIL+URL')
   		thread1.start()
		thread1.join()
		thread2 = Thread(target=start2, args=(site, dork))
		thread2.start()
   		thread2.join()

   else:
	usage()