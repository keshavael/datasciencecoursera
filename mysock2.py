import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))

mysock.send('GET /code/intro-short HTTP/1.1\r\nHost: www.py4inf.com\r\n\r\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()
#mysock.send('GET http://www.py4inf.com/code/intro-short.txt HTTP/1.0\n\n')
