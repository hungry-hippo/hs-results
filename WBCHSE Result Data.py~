import urllib, requests, re, csv, psutil, time, Queue, threading
from bs4 import BeautifulSoup

from threading import Thread
keys = {'SUB6','No.','SUB5','SUB2','Name','SUB1','SUBM1','SUBM2','SUBM3','SUBM4','SUB4','SUBM6','SUBM5','Total','ROLL','SUB3'}


def getroll(intrno):
    return str(intrno).zfill(4)

def getdata(rollno, intrno, url,q):
    flag=0
    student={}
    
    for key in keys:
        student[key]='NONE'
        
    rno=getroll(intrno)
    payload = {'roll': rollno, 'rno': rno, 'B1':'Submit'}
    
    
    headers=dict([('Content-type', 'application/x-www-form-urlencoded'), ('Content-length', '50'), ('Referer', 'http://wbresults.nic.in/highersecondary/wbhsres.htm'), ('Host', 'wbresults.nic.in')])

    for i in range (5): #try again for connection error
        try:
            fp = requests.post(url, data=payload, headers=headers)
            html = fp.content
            soup = BeautifulSoup(html,"html.parser")
            for line in soup.findAll('strong'):
                data = ''.join(line.findAll(text=True))
                if 'Please CHECK the Roll No & Try again' in data.encode('utf-8'):
                    flag=1
                
                  
            if flag == 0:
                x=0
                temp=''
                for line in soup.findAll('strong'):
                    s = ''.join(line.findAll(text=True))
                    s=s.encode('ascii', 'ignore')
                    s=str(s).strip()
                    #print s
                    if temp == 'Grade & Percentile':
                        marks=re.findall(r'\w*(\w\w\w\w)(\w\w\w)\w',s,re.IGNORECASE)
                        k=0
                        for mark in marks:
                            k+=1
                            student['SUB'+str(k)]=mark[0]
                            student['SUBM'+str(k)]=mark[1]
                    if temp == 'ROLL' or temp=='No.' or temp=='Name' or temp=='Total':
                       student[temp] = s.encode('ascii', 'ignore')
                    temp=s
                
                q.put(student)
                
                
            break
            
        except:
            e=open('Error.txt','a')
            e.write('Try: ' + str(i) +' Connection Error at ' + str(rollno) + rno +'\n')
            e.close()

            
def scribe(q):
    
    with open('WBResult.csv','ab') as f:
        w=csv.DictWriter(f,fieldnames=keys, dialect='excel', restval="N/A")
        w.writeheader()
            
        while True:
            student = q.get()
            if student == 'STOP':
                break
            
            elif student:
                w.writerow(student)
        
       
def main():
    url = r'http://wbresults.nic.in/highersecondary/wbhsresult.asp'
    q=Queue.Queue()
    threads=[]
    scribethread=Thread(target=scribe, args=(q,))
    scribethread.daemon=True
    scribethread.start()
    
    f=open('WBRoll.txt','r')
    
    for roll in f.readlines():
        match = re.search(r'(\w*)\n',roll)
        roll=match.group(1)
        print roll
        for rno in range (1001,2501,50):
            
            while psutil.cpu_percent(interval=1) > 90:
                print 'Overuse'
                time.sleep(1)
                
                
            for v in range(0,50):
                try:
                    t=Thread(target=getdata, args=(roll,rno+v,url,q))
                    t.start()
                    threads.append(t)
                except:
                    print "\n\n\nError: unable to start thread\n\n",
                    
            for thread in threads:
                thread.join()  

    q.put('STOP')
    f.close()
    print "DONE"
    
if __name__ == '__main__':
    main()
