import socket
import sys 
import tqdm
from datetime import datetime
from urllib.request import urlparse
import requests


def start_port_scan():
    url = input("Input URL of the web application : ")
    listofopenports = []
    if(filterinput(url) == None):
        target = socket.gethostbyname(url)
    else:
        target = socket.gethostbyname(filterinput(url))
    print("-" * 50) 
    print("Scanning Target: " + url) 
    print("Scanning started at:" + str(datetime.now())) 
    print("-" * 50)
    try: 
      
        # will scan ports between 1 to 65,535 
        for port in tqdm.tqdm(range(1,65535)): 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            socket.setdefaulttimeout(0.5) 
          
            # returns an error indicator 
            result = s.connect_ex((target,port)) 
            if result ==0: 
                listofopenports.append("Port {} is open".format(port)) 
            s.close() 
          
    except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved") 
 
    except socket.error: 
        print("\ Server not responding") 

    for i in listofopenports:
        print(i)



def filterinput(input):
   x = urlparse(input)
   return x.hostname