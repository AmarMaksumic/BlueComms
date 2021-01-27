from bt import init, connect
from config import server_mac, server_port, backlog, size

init(server_mac, server_port, backlog, size)
connect()