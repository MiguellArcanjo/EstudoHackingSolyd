import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(("...", ...))
    client.send(b"oajnsojans")
except:
    print("Não foi possivel estabelecer a conexão")

pacotes_recebidos = client.recv(1024).decode()
print(pacotes_recebidos)