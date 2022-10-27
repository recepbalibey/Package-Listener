import scapy.all as scapy
from scapy_http import http


#Store = do not save the packets to the storage(it is too much packages)
#prn=allows you to pass a function that executes with each packet sniffed. 
#This allows us to do some custom actions with each packet sniffed.

# Be MITM and start listening packets! (use arp_poisoning.py)

def packet_listener(interface):
	scapy.sniff(iface=interface, store=False, prn=analyze_packets)

#HTTP > HTTP Request > Raw > Load  ( checked in the first run )
def analyze_packets(packet):
	if packet.haslayer(http.HTTPRequest):
		if packet.haslayer(scapy.Raw):
			packet[scapy.Raw].load




packet_listener("eth0")
