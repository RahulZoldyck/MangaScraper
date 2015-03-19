import bs4 as BS
import requests
import urllib
import time 
import socket


socket.getaddrinfo('localhost', 8080)

qa=0
print "anime name : "
an=raw_input()
an=an.lower()
an=an.replace (" ", "_")
print "from chapter : "
lo=raw_input()
print "to chapter : "
up=raw_input()


for ch in range(int(lo),int(up)+1):
    qa=0
    print ("chapter "+str(ch))
    t=requests.get("http://mangafox.me/manga/"+an+"/v01/c00"+str(ch)+"/1.html")
    soup=BS.BeautifulSoup(t.text)
    h=soup.findAll("option")
    links = [i['value'] for i in h]
    for i in links:
        if int(i)>qa:
            qa=int(i)
	
	
	
    for p in range(1,qa):
        w=requests.get("http://mangafox.me/manga/"+an+"/v01/c00"+str(ch)+"/"+str(p)+".html")
        soup=BS.BeautifulSoup(w.text)
        r=soup.findAll("img")
        links = [i['src'] for i in r]
        
        for l in links:
            print ("page"+str(p))
            urllib.urlretrieve(l,"Chapter"+str(ch)+"  Page"+str(p)+".png")
            break


