import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.158", 5001))

while True:
    client.send(input("Введите сообщение:").encode())
 