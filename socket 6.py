import socket
s=socket.socket()
s.connect(("127.0.0.1",8080))
s.send(b"HEAD / HTTP/1.0\r\n\r\n")
banner =s.recv(1024).decode()
print("[+] Response:")
print(banner)
s.close()
