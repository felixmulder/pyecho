#!/usr/bin/python

import socket
import time
import threading

def handle_connection(c):
    msg = c.recv(4096).decode("UTF-8")
    print("Received from client:", msg)
    #time.sleep(5)
    c.send(bytes(msg,"UTF-8"))

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
        thread = threading.Thread(target = handle_connection, args = (c, ))
        thread.start()

if __name__ == "__main__":
    main()
