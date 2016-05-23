import BeautifulSoup as BS
import requests
import urllib
import time 
import socket
import sys
import os

socket.getaddrinfo('localhost', 8080)
test=1
qa=0
print "Manga name : "
an=raw_input()
path=an
try:
    os.makedirs(path)
except:
    print "already there!"
an=an.lower()
an=an.replace (" ", "_")
print "from chapter : "
lo=raw_input()
print "to chapter : "
up=raw_input()

for ch in range(int(lo),int(up)+1):
    os.makedirs(os.path.join(path,"Chapter "+str(ch)))
    qa=0
    print ("chapter "+str(ch))
    t=requests.get("http://mangafox.me/manga/"+an+"/v01/c00"+str(ch)+"/1.html")
    soup=BS.BeautifulSoup(t.text)
    h=soup.findAll("option")
    links = [i['value'] for i in h]
    for i in links:
        if int(i)>qa:
            qa=int(i)
	
	
	
    for p in range(1,qa+1):
        test=1
        while(test==1):
            test=0
            try:
                w=requests.get("http://mangafox.me/manga/"+an+"/v01/c00"+str(ch)+"/"+str(p)+".html")
            except:
                test=1
                

        soup=BS.BeautifulSoup(w.text)
        r=soup.findAll("img")
        links = [i['src'] for i in r]
        
        for l in links:
            test=1
            while (test==1):
                test=0
                try:
                    imgname="Chapter"+str(ch)+"  Page"+str(p)+".jpg"
                    fullpath=os.path.join(os.path.join(path,"Chapter "+str(ch)),imgname)
                    print ("page"+str(p))
                    urllib.urlretrieve(l,fullpath)
                except:
                    test=1
                    
            break
                    
                    
                
                
            
            
            
