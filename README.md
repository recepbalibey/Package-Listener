# Package-Listener
Package Listener(Like wireshark) 

This is the other step of MITM attack. 
We are able to be MITM but we also want to see the details of the packet.
We need a packet listener.

In Wireshark, there are tons of packets. We can use the filters to check specific packets but again, it will take too much to find what we need. 

Scapy is a powerful and versatile packet manipulation tool written in python. Using scapy, a user will be able to send, sniff, dissect and forge network packets. Scapy also has the capability to store the sniffed packets in a pcap file. Using scapy, we will be able to handle tasks like trace routing, probing, scanning, unit tests, and network discovery with ease. All of these properties make scapy useful for network-based attacks.

**Packet sniffing** is the process of capturing all the packets flowing across a computer network. The sniffed packets give away a lot of information like what website does a user visit, what contents does the user see, what does the user download and almost everything. The captured packets are usually stored for future analysis.
[More here : link](https://www.geeksforgeeks.org/packet-sniffing-using-scapy/)
The `sniff()` function returns information about all the packets that has been sniffed.
`capture = sniff()`
To see the summary of packet responses, use **summary().**
`capture.summary()`
The `sniff()` function listens for an infinite period of time until the user interrupts.
To restrict the number of packets to be captured sniff() allows a **count** parameter.
`capture = sniff(count=5)`
You can also filter packets while sniffing using the **filter** parameter.
`sniff(filter="tcp", count=5)`
When scapy sniffs packets, it generally sniffs from all of your network interfaces. However, we can explicitly mention the interfaces that we would like to sniff on using the **iface** parameter.
`sniff(iface="eth0", count=5)`
`sniff()` function has another interesting parameter called **prn** that allows you to pass a function that executes with each packet sniffed. This allows us to do some custom actions with each packet sniffed.
`sniff(prn=lambda x:x.summary(), count=5)`
Scapy also allows us to store the sniffed packets in a **pcap** file. 
`wrpcap("<file name>", capture)`

This is great for HTTP but not HTTPS!

For HTTPS:
SSLstrip + dns2proxy
We need IP forwarding. dns2proxy will need process the packets.
We will forward to it. SSLstrip works in port 10000. dn2proxy works in 53.

```
┌──(root㉿linuxkali)-[~]
└─# iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53
```

```
┌──(root㉿linuxkali)-[~]
└─# iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
```

``` 
┌──(root㉿linuxkali)-[/opt/dnstest]
└─# git clone https://github.com/singe/dns2proxy.git
Cloning into 'dns2proxy'...
remote: Enumerating objects: 155, done.
remote: Total 155 (delta 0), reused 0 (delta 0), pack-reused 155
Receiving objects: 100% (155/155), 45.55 KiB | 548.00 KiB/s, done.
Resolving deltas: 100% (85/85), done.

