import socket
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("Server waiting for connections...")
client, addr = server.accept()
print("Connected with", addr)
client.send(bytes("Hello Client! Welcome to the server.", 'utf-8'))
client.close()
