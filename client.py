import socket
import cv2
import sys

ip = sys.argv[1] #server ip
port = int(sys.argv[2]) #server port
camera_num = int(sys.argv[3])   #camera number

cap = cv2.VideoCapture(camera_num)
BUFFER_SIZE = 4096
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        jpegstring=cv2.imencode('.jpeg', frame,encode_param)[1].tobytes()

        s.sendto(jpegstring,(ip,port))