from bt import init, connect, send
from config import server_mac, server_port
import tkinter as tk

def pass_input():
  send(inputtxt.get(1.0, "end-1c"))

init(server_mac, server_port)
connect()

window = tk.Tk()

window.title("Input")

inputtxt = tk.Text(window, 
                   height = 5, 
                   width = 40) 
  
inputtxt.pack() 
  
printButton = tk.Button(window, 
                        text = "Send",  
                        command = pass_input) 
printButton.pack() 

window.mainloop()