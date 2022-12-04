import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port_number = 8000

server.bind((ip, port_number))

server.listen()
print("Server has started")

client = []
names = []

def broadcast(message, data):
    for i in client:
        if i != data:
            i.send(message.encode('utf-8'))  

def remove(data):
    if data in client:
        client.remove(data)

def nameRemove(name):
     if name in names:
        names.remove(name)

def client_thread(data, name):
    message = 'Welcome to the chat room!'
    data.send(message.encode('utf-8'))
    while True:
        msg = data.recv(1024).decode('utf-8')
        if msg:
            print(name+" says: "+msg)
            send = name+" says: "+msg
            broadcast(send, data)
        else:
            remove(data)
            nameRemove(name)  

while True:
    data, addr = server.accept()
    data.send('name'.encode('utf-8'))
    name = data.recv(1024).decode('utf-8')
    client.append(data)
    names.append(name)
    print(name+' connected to socket')
    msg = name+ 'connected to socket'
    broadcast(msg, data)
    thread = Thread(target=client_thread, args=(data, name))
    thread.start()