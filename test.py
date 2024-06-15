import socket
import selectors

selector = selectors.DefaultSelector()


def server_sock():
    host = '0.0.0.0'
    port = 5001
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
    server.bind((host, port))
    server.listen()
    selector.register(fileobj=server, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server):
    print("Запуск!")
    client, adr = server.accept()
    print(f"Есть подключение{adr[0]}:{adr[1]}")
    selector.register(client, selectors.EVENT_READ, data=send_message)


def send_message(client):
    request = client.recv(1024).decode()
    if request:
        print(request)
        response = b'ok'
        client.send(response)
    else:
        selector.unregister(client)
        client.close()


def event_loop():
    while True:
        events = selector.select()
        for key, value in events:
            call = key.data
            call(key.fileobj)


event_loop()
