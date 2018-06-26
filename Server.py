import socket
import cv2
import numpy
#logic for buffer creation how to allocate a space for that buffer..
def call(sock, count):
    buf = b''
    while count:
        buff = sock.recv(count)
        if not buff: return None
        buf += buff
        count -= len(buff)
    return buf

TCP_IP = '192.168.0.102'
TCP_PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)
conn, addr = s.accept()

length = int(call(conn,16))
stringData = call(conn, length)
data = numpy.fromstring(stringData, dtype='uint8')
s.close()

decimg=cv2.imdecode(data,1)
cv2.imshow('SERVER',decimg)
cv2.imwrite("D:\\a"+".jpg",decimg) #here this path image will be stored 
cv2.waitKey(0)
cv2.destroyAllWindows()
