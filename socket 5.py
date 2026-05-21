import socket
try:
    target_url= input("Enter website name:")
    target_ip = socket.gethostbyname(target_url)
    print(f"[+]The IP address of {target_url} is{ target_ip}")
except socket.gaierror:
    print("[-]Invalid website or DNS lookup failed")
