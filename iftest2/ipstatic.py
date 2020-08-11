#!/usr/bin/env python3
ipchk = input("Applying an IP ADDRESS: ")

# a string tests as True
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the gateway was set: " + ipchk + "this is not recommended")
elif ipchk:
    print("lets go network connectivity! : " + ipchk)
else: 
    print("you didnt provide the data butthead")
