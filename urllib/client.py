import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('localhost',4000))

msg=s.recv(1024)

while msg:
    msg=s.recv(1024)
    print("received: ",msg.decode())
    

s.close()