#!/usr/bin/env python

import argparse
#import socket
import subprocess
import sys
#from datetime import datetime

class Device:
    def __init__(self, name, ipaddr, mac, interface):
        self.name = name
        self.ipaddr = ipaddr
        self.mac = mac
        self.interface = interface

    def __repr__(self):
        return "Device({},{},{},{})".format(self.name, self.ipaddr, self.mac, self.interface)

    def __str__(self):
        return "Device name: {}\nIP address: {}\nMAC address: {}\nInterface: {}".format(self.name, self.ipaddr, self.mac, self.interface)

devices = []

def create_dev(d):
    attr = d.split(' ')
    return Device(attr[0], attr[1][1:-1], attr[3], attr[5])


# arp = ['arp', '-a']

# result = subprocess.check_output(arp)

# devs = result.split('\n')
#print(devs)
# devs.pop()

# for d in devs:
#     devices.append(create_dev(d))


#dvs = devs[0].split()


#for i in range(len(dvs)):
#    print(str(i) + ' = ' + dvs[i])

#print(devices)
# print(devices[0])
#for d in devices:
#    print(devices)

def print_usage():
    print("Usage: python lanchat.py [-h] [-s] [-c]")

# def parse_args():

def print_help():
    print_usage()
    print("  -s\tscan devices on network")
    print("  -c\tchat with devices on network")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    if sys.argv[1] == '-h':
        print_help()
        return

    if sys.argv[1] == '-s':
        #scan
        print('scan')
    
    if sys.argv[1] == '-c':
        print('chat')

if __name__ == '__main__':
    main()