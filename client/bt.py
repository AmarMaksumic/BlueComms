import socket

server_mac = server_port = s = None

def init(mac, port):
  global server_mac
  global server_port
  server_mac = mac
  server_port = port

def connect():
  global s
  s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
  s.connect((server_mac, server_port))

def send(message):
  s.send(message.encode('utf-8'))

def disconnect():
  s.close()