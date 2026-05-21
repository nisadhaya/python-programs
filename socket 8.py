from scapy.all import IP, TCP

# Create the packet: IP layer (Layer 3) with TCP layer (Layer 4) on top
packet = IP(dst="172.16.18.65") / TCP(dport=80)

print(f"[+] Packet structure: {packet.summary()}")
