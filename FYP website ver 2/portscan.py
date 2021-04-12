import socket
import sys
import nmap
import json


try:
    target = socket.gethostbyname(sys.argv[1])
    print(target)
    nm = nmap.PortScanner()
    nm.scan(target,'1-500')
except:
    print("Error has occured")


for host in nm.all_hosts():
     print("Host : %s (%s)" % (host,target))
     print("State : %s" % nm[host].state()) #get state of host(up|down|unknown|skipped)
     # now write the loop for finding the protocol
     for proto in nm[host].all_protocols(): #get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
          print("----------" * 6)
          print("Protocol : %s" % proto)
          lport = nm[host][proto].keys() #get all ports for tcp/udp protocol
          for port in sorted(lport):
             print ("port : %s\tstate : %s" % (port,nm[host][proto][port]['state']))


