#!/usr/bin/python

import socket
import time
import threading

class MessageHandler(threading.Thread):
    def connection(self, c):
        self.c = c 

    def run(self):
        msg = self.c.recv(4096).decode("UTF-8")
        print("Received from client:", msg)
        time.sleep(5)
        self.c.send(bytes(msg,"UTF-8"))

def main(argv = None):
    host = "127.0.0.1"
    if argv == None:
        port = 1337
    else:
        port = argv[1]

    s = socket.socket()
    s.bind((host,port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Connection from", addr)
        handler = MessageHandler()
        handler.connection(c)
        handler.start()

if __name__ == "__main__":
    main()
