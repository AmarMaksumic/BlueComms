import socket
import pyperclip as pc 

server_mac = server_port = backlog = size = window = None

def init(mac, port, log, s):
  global server_mac
  global server_port
  global backlog
  global size
  server_mac = mac
  server_port = port
  backlog = log
  size = s

def connect():
  bt_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
  print(server_mac)
  print(server_port)
  bt_socket.bind((server_mac, server_port))
  bt_socket.listen(backlog)
  try:
      client, address = bt_socket.accept()
      while 1:
          data = client.recv(size)
          if data:
              print(data.decode('utf-8'))
              pc.copy(data.decode('utf-8'))
              client.send(data)
  except:	
      print("Something is wrong...closing socket")	
      client.close()
      bt_socket.close()