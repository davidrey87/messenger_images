from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from PIL.ImageQt import ImageQt
from PIL import Image
import io

def connection():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = s.accept()
        print("%s:%s se ha conectado." % client_address)
        #client.send(("Bienvenido...").encode("utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, client_address,)).start()

def handle_client(client, client_address):  # Takes client socket as argument.
  """Handles a single client connection."""
  #name = client.recv(BUFFER_SIZE)
  #clients[client] = name
  while True:
    msg = client.recv(BUFFER_SIZE)
    img = open('screenshottmp.png','wb')
    img.write(msg)
    #buffer_img = io.BytesIO(msg)
    #img = Image.open(buffer_img)


    broadcast(client_address, msg)

def broadcast(client_address,msg):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in addresses:
        #print(sock.getpeername())
        #print(client_address)
        if sock.getpeername() != client_address:
            img = open("screenshottmp.png","rb")
            sock.sendfile(img)

clients = {}
addresses = {}
HOST = '127.0.0.1'
PORT = 1235
BUFFER_SIZE = 800000  
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))

if __name__ == "__main__":
  s.listen(2)
  print("Esperando Conexiones...")
  incomeClient = Thread(target=connection)
  incomeClient.start()
  incomeClient.join()
