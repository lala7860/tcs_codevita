import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []

# create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error: " + str(msg))

# binding the socket and listning for connections
def bind_socket():
    try:
        global host
        global port 
        global s
        print("binding the port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error: " + str(msg) +"\n"+ "retrying...")
        bind_socket()

# reading connections from multiple clients and saving to a list
# closing previous connections when server.py file is restarted

        