import socket
from select import select

host = '0.0.0.0'
port = 5001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
server.bind((host, port))
server.listen()

tasks = []


def accept_connection(server):
    print("Запуск!")
    client, adr = server.accept()
    print(f"Есть подключение{adr[0]}:{adr[1]}")
    tasks.append(client)


def send_message(client):
    request = client.recv(1024).decode()
    if request:
        print(request)
        response = b'ok'
        client.send(response)
    else:
        client.close()


def event_loop():
    while True:
        ready, _, _ = select(tasks, [], [])
        for sock in ready:
            if sock is server:
                accept_connection(sock)
            else:
                send_message(sock)


tasks.append(server)
event_loop()
