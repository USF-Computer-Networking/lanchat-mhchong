# LAN Scan and Chat

## Design motivation
The scanning and UDP chat code is placed in a single Python script with the idea of a Swiss Army knife design. These features are commonly placed in seperate files. However, this design promotes portability of the code without having to worry about a missing Python script. Think of this program as an all-in-one utility.

## Scan for Devices

Usage:
```
$ python lanchat.py -s
```
The command above will display all devices on the same network as your device. Information such as device name, IP address, MAC address and interface will be displayed.

This feature is achieved by using the subprocess module of python to invoke the arp command.

## UDP Chat
To listen for messages:
```
$ python lanchat.py -c
Enter l to start server
Enter s to send message
Action: l
```

To send messages:
```
$ python lanchat.py -c
Enter l to start server
Enter s to send message
Action: s
```

### TODOs:
- Support user provided IP address
- Better command line interface design / user interaction