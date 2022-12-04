import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = input("Enter your username: ")

ip = '127.0.0.1'
port_number = 8000

client.connect((ip, port_number))

print("Connected to "+ip+"at port"+str(port_number))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'name':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("Connection to server lost :(")
            client.close()
            break

recv_thread = Thread(target=receive)
recv_thread.start()

def write():
    while True:
        message = input("Send a message -> ")
        client.send(message.encode('utf-8'))

write_thread = Thread(target=write)
write_thread.start()