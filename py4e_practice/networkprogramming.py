#socket is the connection between your device and a service on the internet 
#you must invoke the socket library before using it 

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #I don't understand what all this is 
mysock.connect(('data.pr4e.org', 80))                       #this is saying dear socket, please connect me to port 80 (the http port) on this service
                #phone number and ext

#HTTP - hypertext transfer protocol
#a web url is split into 3 parts 
# [http://]   [www.dr-chuck.com]     [/page1.htm]
# protocol       host                   document to retrieve
