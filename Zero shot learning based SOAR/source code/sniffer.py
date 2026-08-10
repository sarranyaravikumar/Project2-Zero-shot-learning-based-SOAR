from scapy.all import sniff, IP

def process(packet):
    if packet.haslayer(IP):
        print(f"{packet[IP].src} → {packet[IP].dst}")

sniff(prn=process, store=0)