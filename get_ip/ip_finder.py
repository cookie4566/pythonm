# IP finder! 
# use this program to find an IP of any website
#version 0.1

import socket
import sys

# socket creation
try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     print("socket creation successful")
except socket.error as err:
     print("socket creation failed with error %s" %(err))
# default socket port
port = 80

try:
    print("Enter a domain for an IP search.")
    print("Make sure you start with www and end with .com!")
    web_site = input()
    host_ip = socket.gethostbyname(web_site)
except socket.gaierror:
    
    print ("error resolving to host")
    sys.exit
    
s.connect((host_ip, port))

print("the socket has successfully connected!")
print(host_ip)