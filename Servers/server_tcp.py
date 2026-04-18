import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file = open("output.txt", "w")

try:
    server.bind(("0.0.0.0", 4430))
    server.listen(5)
    print("Listening...")

    client_socket, address = server.accept()
    print(f"Received from: {address[0]}")

    data = client_socket.recv(1024).decode()

    file.write(data)

#    while True:
#        data = client_socket.recv(1024).decode()
#        if data == "senhasecreta\n":
#            client_socket.send(b"Mensagem secreta")
    server.close()
except Exception as error:
    print("Ocorreu um erro", error)