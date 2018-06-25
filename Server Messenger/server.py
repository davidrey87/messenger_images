from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def connection():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = s.accept()
        print("%s:%s se ha conectado." % client_address)
        client.send(("Bienvenido...").encode("utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument.
  """Handles a single client connection."""
  name = client.recv(BUFFER_SIZE)
  clients[client] = name
  while True:
    msg = client.recv(BUFFER_SIZE)
    broadcast(msg, name+(": ").encode())

def broadcast(msg, prefix):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(prefix+msg)

clients = {}
addresses = {}
HOST = '127.0.0.1'
PORT = 1234
BUFFER_SIZE = 2000  
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))

if __name__ == "__main__":
  s.listen(2)
  print("Esperando Conexiones...")
  incomeClient = Thread(target=connection)
  incomeClient.start()
  incomeClient.join()
