import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(4, 640)
cam.set(6, 480)

camera = True
f = open("demofile2.txt", "a")


while camera == True:
    success, frame = cam.read()

    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        f.write(i.data.decode('utf-8'))
        f.write('\n')
        time.sleep(6)

    cv2.imshow("OurQr_code_Scanner", frame)
    cv2.waitKey(1)