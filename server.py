import socket
import numpy
import sys
import cv2

BUFFER_SIZE = 4096*10

buf = b''

class capture():
    def __init__(self,port):
        self.port = port

    def recive(self):
        global buf
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while True:
                s.bind(("0.0.0.0", self.port))
                try:
                    data,address = s.recvfrom(BUFFER_SIZE)
                    if not data:
                        break
                    buf = buf + data

                finally:
                    s.close()

                narray=numpy.frombuffer(buf,dtype='uint8')
                buf = b""
                return cv2.imdecode(narray,1)
    def show(self):
        while True:
            img = self.recive()
            cv2.imshow('Capture',img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            img = ''

cap = capture(int(sys.argv[1]))
cap.show()