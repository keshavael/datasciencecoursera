import socket
mysok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysok.connect('data.pr4e.org', 80))

mysok.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data=mysok.recv(512)
    if (len(data)<1):
        break
    print(data)
mysok.close()

#mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/2.4.7\n\n')
