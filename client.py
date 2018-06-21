import socket
import cv2
import numpy

TCP_IP = 'put ip address'
TCP_PORT = 'put port number'
factor=0.75
sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
face_cascade = cv2.CascadeClassifier("D:\\haarcascade_frontalface_alt2.xml")
count=0
capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, None,fx=factor,fy=factor,interpolation=cv2.INTER_AREA)
    face_rects = face_cascade.detectMultiScale(frame, 1.3, 2)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (3400,1234,2500), 5)
        sub_face = frame[y:y+h, x:x+w]
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        #encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', sub_face, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()
        if count==1:
            print(count)
            sock.send( str(len(stringData)).ljust(16).encode('utf-8'));
            sock.send( stringData );
            sock.close()
        count=count+1
    decimg=cv2.imdecode(data,1)
    cv2.imshow('CLIENT',decimg)
    cv2.waitKey(1)
cv2.destroyAllWindows() 
