from PyQt4 import QtGui,QtCore
from PIL.ImageQt import ImageQt
from PIL import Image
import sys
import cliente_ui
import pyscreenshot as ImageGrab
from socket import AF_INET, socket, SOCK_STREAM
import time
import base64
import io

#
# Archivo de Configuracion
#
archivo = open("config.ini", "r")

#
# Cargamos HOST, PORTMSJ, PORTIMG, NOMBRE de un archivo de configuracion
#
HOST = archivo.readline().rstrip()
PORTMSJ = int(archivo.readline())
PORTIMG = int(archivo.readline())
NOMBRE = archivo.readline().rstrip()
BUFFER_SIZE = 800000

#
#Socket para servidor de mensajes
#
socket_msj = socket(AF_INET, SOCK_STREAM)
socket_msj.connect((HOST, PORTMSJ))
socket_msj.send((NOMBRE).encode("utf-8")) #Enviamos el nombre para que identifique al participante del chat

#
#Socket para servidor de imagenes
#
socket_img = socket(AF_INET, SOCK_STREAM)
socket_img.connect((HOST, PORTIMG))

#
# Hilo Pricipal, Carga toda la interfaz grafica y funciones necesarias, asi como sub-hilos
#
class ClienteChatSlides(QtGui.QMainWindow, cliente_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ClienteChatSlides, self).__init__(parent)
        self.setupUi(self)

        ###Inicializando componentes UI

        self.enviar.clicked.connect(self.enviar_mensaje)
        self.transmitir.clicked.connect(self.enviar_imagen)
        self.detener.clicked.connect(self.detener_imagen)

        ###Inicializando hilos

        self.HiloMensajes = RecibirMensaje(self)
        self.connect(self.HiloMensajes,QtCore.SIGNAL("agregar_mensaje ( QString ) "), self.agregar_mensaje)
        self.HiloMensajes.start()

        self.HiloImagenEnviar = EnviarImagen(self)

        self.HiloImagenRecibir = RecibirImagen(self)
        self.connect(self.HiloImagenRecibir,QtCore.SIGNAL("agregar_imagen ( ) "), self.agregar_imagen)
        self.HiloImagenRecibir.start()

    #
    # Mensaje
    #
    def enviar_mensaje(self):
        socket_msj.send(self.mensaje.toPlainText().encode("utf-8"))
        self.mensaje.clear()

    def agregar_mensaje(self,datos):
        self.chat.appendPlainText(datos)

    #
    # Imagen
    #
    def enviar_imagen(self):
        self.HiloImagenEnviar.start()

    def detener_imagen(self):
        self.HiloImagenEnviar.stop()

    def agregar_imagen(self):
        #img = bytes_a_imagen(datos)
        #img.save('screenshot.png')
        escena =  QtGui.QGraphicsScene()
        escena.addPixmap(QtGui.QPixmap('screenshottmprv.png'))
        self.pantalla.setScene(escena)

#
#Sub-hilo para recibir imagenes
#
class RecibirMensaje(QtCore.QThread):
        def __init__(self,parent=None):
            QtCore.QThread.__init__(self,parent)
        
        def run(self):
            while True:
                datos = socket_msj.recv(BUFFER_SIZE)
                self.emit(QtCore.SIGNAL("agregar_mensaje( QString )"),datos.decode("utf-8"))

#
#Sub-hilo para enviar imagenes
#
class EnviarImagen(QtCore.QThread):
        def __init__(self,parent=None):
            QtCore.QThread.__init__(self,parent)
        
        def run(self):
            while True:
                img =ImageGrab.grab(bbox=(683,1,1366,768)) # X1,Y1,X2,Y2
                #socket_img.sendall(imagen_a_bytes(img))
                img.save('screenshottmp.png')
                fileimg = open("screenshottmp.png","rb")
                socket_img.sendfile(fileimg)
                time.sleep(4)

#
#Sub-hilo para recibir imagenes
#
class RecibirImagen(QtCore.QThread):
        def __init__(self,parent=None):
            QtCore.QThread.__init__(self,parent)
        
        def run(self):
            while True:
                datos = socket_img.recv(BUFFER_SIZE)
                img = open('screenshottmprv.png','wb')
                img.write(datos)
                self.emit(QtCore.SIGNAL("agregar_imagen( )"),  )

#
# Tratamiento de imagenes para enviar y recibir por socket
#      
def bytes_a_imagen(datos):
    buffer_img = io.BytesIO(datos)
    img = Image.open(buffer_img)
    return img

def imagen_a_bytes(img):
    buffer_img = io.BytesIO()
    img.save(buffer_img, format='png')
    return buffer_img.getvalue()

#
#Main
#
def main():
    app = QtGui.QApplication(sys.argv)
    form = ClienteChatSlides()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()