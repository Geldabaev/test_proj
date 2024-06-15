import socket

host = "0.0.0.0"
post = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname_ex(socket.gethostname())[-1][-1])
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((host, post))
server.listen()

while True:
    print("ZAPUSK!")
    client, adr = server.accept()
    print(f"Connect {adr[0]}:{adr[1]}")
    #
    # request = client.recv(1024).decode()
    # if request:
    #     print(request)
    #     response()