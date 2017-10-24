#!/usr/bin/env python
import cv2, time
import numpy as np
import os
import sys
import subprocess


command = "v4l2-ctl --device=/dev/video0 --set-ctrl=led1_mode=0"
import subprocess
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]


video = cv2.VideoCapture(0)
ret = video.set(3, 1024)
ret = video.set(4, 576)
ret = video.set(cv2.cv.CV_CAP_PROP_FPS, 30)

def foo(event, x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
                today=time.time()
                file = "/home/pi/saves/image" + str(today) + ".jpg"
                cv2.imwrite(file,frame)
                print("jpg saved")
  
        if event == cv2.EVENT_RBUTTONDOWN:
                today = time.time()
                file = "/home/pi/saves/image" + str(today) + ".png"
                cv2.imwrite(file,frame)
                print("Image Saved")

cv2.namedWindow('input',13)
cv2.moveWindow('input',0,0)


while True:
        check, frame = video.read()
        cv2.setMouseCallback('input',foo)
        cv2.imshow('input', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if cv2.waitKey(1) & 0xFF == ord('p'):
                print ('thats a p')


video.release()
cv2.destroyAllWindows()

