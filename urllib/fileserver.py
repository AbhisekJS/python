import socket

host= 'localhost'
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print('Server listening to Port: ,',port)

s.listen()

(c,addr) = s.accept()

filename=c.recv(1024)

try:
    f= open(filename,'rb')
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    
    c.send(b"file doesnot exist")
c.close()