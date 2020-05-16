import socket
 
# Create a TCP based client socket
echoClient =  socket.socket();
 
# Note: No need for bind() call in client sockets...
# Just use the socket by calling connect()
echoClient.connect(("localhost", 4000));
 
# Send a message
echoClient.send("Learning Python is fun".encode());
 
# Get the reply 
msgReceived = echoClient.recv(1024);
 
# Print the reply
print("At client: %s"%msgReceived.decode());