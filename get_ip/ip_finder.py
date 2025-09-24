# IP finder! 
# use this program to find an IP of any website
# Now with GUI!
#version 0.3

import socket
from tkinter import *
import sys

# Windoe creation
win = Tk()

# socket creation
try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     print("socket creation successful")
except socket.error as err:
     print("socket creation failed with error %s" %(err))
# default socket port
port = 80

#entry field for domain with label
ip_label = Label(win, text='Website').grid(row = 0)
ip_entry = Entry(win).grid(row = 0, column = 1)
ip_button = Button(win, text='Find IP address').grid(row=0, column=2)


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

win.mainloop()