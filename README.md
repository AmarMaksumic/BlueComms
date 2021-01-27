# BlueComms
Win 10 to RPi text communication over BlueTooth

## Requirements
Packages are listed in requirements.txt. Must be running python 3.9.0 for BlueTooth permissions, and devices must be paired beforehand to ensure connectivity!

## What is the server, and what is the client?
The client is the device you will be sending data from. The server is the device that you will be receiving data on. The server device must have its <i><b>BlueTooth</b></i> MAC address listed in the config.py files of both the server and client.

## How do I use the program?
After setting up the respective code in the client and server devices, run the main.py file on each. On the client device, a GUI will appear in which you can enter and send text by hitting 'Send.' On the server device, the text will simply be appended to the device's clipboard.
