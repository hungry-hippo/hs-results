#!/usr/bin/python

import urllib, requests, re, csv, psutil, time, Queue, threading
from bs4 import BeautifulSoup

from threading import Thread

def getdata(rollno, url,q):
    payload = {'roll': rollno, 'rno': '1001', 'B1':'Submit'}
    #print rollno
    
    headers=dict([('Content-type', 'application/x-www-form-urlencoded'), ('Content-length', '50'), ('Referer', 'http://wbresults.nic.in/highersecondary/wbhsres.htm'), ('Host', 'wbresults.nic.in')])

    for i in range (5): #try again for connection error
        try:
            fp = requests.post(url, data=payload, headers=headers)
            html = fp.content
            soup = BeautifulSoup(html,"html.parser")
            for line in soup.findAll('strong'):
                data = ''.join(line.findAll(text=True))
		 
                if 'Please CHECK the Roll No & Try again' in data.encode('utf-8'):
                    return
            q.put(rollno)
	    #print rollno 
            break    
            
        except:
            e=open('Error_Roll.txt','a')
            e.write('Try: ' + str(i) +' Connection Error at ' + str(rollno) + '\n')
            e.close()
            time.sleep(1)

            
def scribe(q):
    # first_time
    with open('WBRoll.txt','a') as f:
	while True:
	        roll = q.get()
	        if roll == 'STOP':
	            f.close()
	            break
	        f.write(str(roll)+'\n')
		print 'Valid:',roll
        
        





def main():
    url = r'http://wbresults.nic.in/highersecondary/wbhsresult.asp'
    q=Queue.Queue()
    threads=[]
    scribethread=Thread(target=scribe, args=(q,))
    scribethread.daemon=True
    scribethread.start()
    for roll in range (1001,9999,10):
        while psutil.cpu_percent(interval=1) > 90:
            print 'Overuse'
            time.sleep(1)
        for k in range(10):  
            for v in (11,12,13,21,22,23):
                try:
                    t=Thread(target=getdata, args=(str(roll+k)+str(v),url,q))
                    t.start()
                    threads.append(t)
                except:
                    print "\n\n\nError: unable to start thread\n\n",
         
        for thread in threads:
            thread.join()  

    q.put('STOP')
    print "DONE"
    
if __name__ == '__main__':
    main()
