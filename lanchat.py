#!/usr/bin/env python
''' 
    lanchat.py

    A program that supports scanning and UDP chat

    Scanning is achieved by using the subprocess module
    to invoke the arp command

    UDP chat is achieved using the socket module for
    sending and receving messages
'''

import socket
import subprocess
import sys


class Device:
    def __init__(self, name, ipaddr, mac, interface):
        self.name = name
        self.ipaddr = ipaddr
        self.mac = mac
        self.interface = interface

    def __repr__(self):
        return "Device({},{},{},{})".format(self.name, self.ipaddr, self.mac, self.interface)

    def __str__(self):
        return "Device name: {}\nIP address: {}\nMAC address: {}\nInterface: {}\n".format(self.name, self.ipaddr, self.mac, self.interface)


def create_dev(d):
    attr = d.split(' ')
    return Device(attr[0], attr[1][1:-1], attr[3], attr[5])

def print_usage():
    '''
    Print program usage
    '''
    print("Usage: python lanchat.py [-h] [-s] [-c]")

def print_help():
    '''
    Display help for the program
    '''
    print_usage()
    print("  -s\tscan devices on network")
    print("  -c\tchat with devices on network")


def scan():
    cmd = ['arp', '-a']
    result = subprocess.check_output(cmd)
    devs = result.split('\n')
    devs.pop()
    devices = []
    for d in devs:
        devices.append(create_dev(d))
    
    for d in devices:
        print(d)



def server(ip='localhost', port=8080):
    '''
    Listen for messages sent by client
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    server_address = ('localhost', 8080)
    server_address = (ip, port)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    while True:
        try:
            print('waiting to receive message')
            data, address = sock.recvfrom(4096)
            print('received %s bytes from %s' % (len(data), address))
            print(data)
            if data:
                sent = sock.sendto(data,address)
                print('sent %s bytes back to %s' % (sent, address))
        except KeyboardInterrupt:
            print('\nShutting down server...')
            sock.close()
            break



def client(ip='localhost', port=8080):
    '''
    Send messages to a listening device/port
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server_address = ('localhost', 8080)
    server_address = (ip, port)
    message = 'Incoming message'

    try:
        print('sending "%s"' % message)
        sent = sock.sendto(message, server_address)
        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        print('received "%s"' % data)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
    finally:
        print('closing socket')
        sock.close()

def chat():
    print('Listen or Send?')
    print('Enter l to start server')
    print('Enter s to send message')
    user_input = raw_input('Action: ')
    if user_input == 'l':
        server()
    elif user_input == 's':
        client()
    else:
        print('Error, invalid input')
        print('Terminating...')
        return

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    if sys.argv[1] == '-h':
        print_help()
        return

    if sys.argv[1] == '-s':
        #scan
        #print('scan')
        scan()
    
    if sys.argv[1] == '-c':
        #print('chat')
        chat()

if __name__ == '__main__':
    main()
