import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('localhost',4000))

filename= input("Enter a file Name: ")

s.send(filename.encode())

content= s.recv(1024)

print(content.decode())
    

s.close()