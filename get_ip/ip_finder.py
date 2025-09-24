# IP finder! 
# use this program to find an IP of any website
# Now with GUI!
#version 0.3

import socket
from tkinter import *
import sys

# Windoe creation
win = Tk()
# string 

# socket creation
try:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     print("socket creation successful")
except socket.error as err:
     print("socket creation failed with error %s" %(err))
# default socket port
port = 80

def find_ip():
    weba = ip_entry.get()
    try:
        print("Enter a domain for an IP search.")
        print("Make sure you start with www and end with .com!")
        host_ip = socket.gethostbyname(weba)
    except socket.gaierror:
    
        print ("error resolving to host")
        sys.exit
    
    s.connect((host_ip, port))

    print("the socket has successfully connected!")
    print(host_ip)
#nessacery widgets(entry field buttons and labels)
ip_label = Label(win, text='Website').grid(row = 0)
ip_entry = Entry(win).grid(row = 0, column = 1)
ip_button = Button(win, text='Find IP address', command=find_ip).grid(row=0, column=2)
exit.button = Button(win, text='exit',command= win.destroy).grid(row=0, column=3)
note_label = Label(win, text='Enter a domain for an IP search.').grid(row=1)
note_label2 = Label(win, text='"Make sure you start with www and end with .com!').grid(row=2)



win.mainloop()