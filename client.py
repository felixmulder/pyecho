#!/usr/bin/python

"""
usage: pass a string as an argument to the program
"""

import sys
import getopt
import socket

# local config
import config

def send(msg):
    b = bytes(msg, "UTF-8")
    s = socket.socket()

    s.connect((config.HOST,config.PORT))
    s.send(b)
    resp = s.recv(4096).decode("UTF-8")
    s.close()
    return resp

def main(argv = None):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)

    msg = " ".join(sys.argv[1:])
    response = send(msg)
    print(response)

if __name__ == "__main__":
    main()
