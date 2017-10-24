from Tkinter import *
import tkMessageBox
import subprocess
import os

vidnum = 0

#def backlightcompensation():
    #v4l2-ctl -d /dev/video0 --set-ctrl  backlight_compensation=0 or 1


def setsharpness(numVal):
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl sharpness=" + str(numVal)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0, END)
    colorLog.insert(0.0, "Sharpness " + str(numVal))

def startcamera():
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Camera Started \n")
    os.system ("python snapshot0.py &")

def setautofocus_on():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl focus_auto=1"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    statemsg = "Turning on Auto focus"
    colorLog.delete(1.0, END)
    colorLog.insert(0.0, statemsg)

def setautofocus_off():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl focus_auto=0"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    statemsg = "Turning off Auto focus"
    colorLog.delete(1.0, END)
    colorLog.insert(0.0, statemsg)

def checkfocusstate(x):
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --get-ctrl focus_auto"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return str(output)

def adjfocus(numVal):
    myval2 = checkfocusstate(0)
    if myval2 != 'focus_auto: 1\n':
        command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl focus_absolute=" + str(numVal)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        colorLog.delete(1.0, END)
        colorLog.insert(0.0, "Focus is set to " + str(numVal))
    else:
        colorLog.delete(1.0, END)
        colorLog.insert(0.0, "Auto Focus is on")

def setautoexposure_on():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl exposure_auto=3"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    statemsg = "Turning on Auto Exposure"
    colorLog.delete(1.0, END)
    colorLog.insert(0.0, statemsg)

def setautoexposure_off():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl exposure_auto=1"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    statemsg = "Turning off Auto Exposure"
    colorLog.delete(1.0, END)
    colorLog.insert(0.0, statemsg)

def checkexposurestate(x):
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --get-ctrl exposure_auto"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return str(output)

def adjexposure(numVal):
    myval = checkexposurestate(0)
    if myval != 'exposure_auto: 3\n':
        command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl exposure_absolute=" + str(numVal)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        colorLog.delete(1.0, END)
        colorLog.insert(0.0, "Exposure set to " + str(numVal))
    else:
        colorLog.delete(1.0, END)
        colorLog.insert(0.0, "Auto Exposure is on")

def tiltcamera(numVal):
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl tilt_absolute=" + str(numVal)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0, END)
    colorLog.insert(0.0, "Tilt " + str(numVal))

def pancamera(numVal):
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl pan_absolute=" + str(numVal)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Pan " + str(numVal))

def listcameras():
    command="v4l2-ctl --list-devices"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, output)

def ledoff():
    command="v4l2-ctl --device=/dev/video" + str(vidnum) + " --set-ctrl=led1_mode=0"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "LED Off \n")

def zoom100():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl zoom_absolute=100"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Zoom 100 \n")

def zoom200():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl zoom_absolute=200"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Zoom 200 \n")
    
def zoom300():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl zoom_absolute=300"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Zoom 300 \n")

def zoom400():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl zoom_absolute=400"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Zoom 400 \n")

def zoom500():
    command="v4l2-ctl -d /dev/video" + str(vidnum) + " --set-ctrl zoom_absolute=500"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    colorLog.delete(1.0,END)
    colorLog.insert(0.0, "Zoom 500 \n")

def toggle():
    if 'On' in str(t_btn.config('text')):
        nt = setautoexposure_off()
        t_btn.config(text='Auto Exposure:Off')
    else:
        nt = setautoexposure_on()
        t_btn.config(text='Auto Exposure:On')

def toggle2():
    if 'On' in str(t_btn2.config('text')):
        nt = setautofocus_off()
        t_btn2.config(text='Auto Focus:Off')
    else:
        nt = setautofocus_on()
        t_btn2.config(text='Auto Focus:On')

#user_input = raw_input("Enter camera number to control: ")
user_input = '0'
if user_input  == '0':    
    root = Tk()
    root.wm_title("Camera Controller")
    root.attributes('-topmost', True)
    
    #Right Frame and its contents
    rightFrame = Frame(root, width=200, height = 600)
    rightFrame.grid(row=0, column=1, padx=0, pady=2)

    btnFrame = Frame(rightFrame, width=200, height = 200)
    btnFrame.grid(row=1, column=0, padx=0, pady=2)

    colorLog = Text(rightFrame, width = 60, height = 5, takefocus=0)
    colorLog.grid(row=2, column=0, padx=10, pady=2)

    redBtn = Button(btnFrame, width=10, text="Zoom 100", command=zoom100)
    redBtn.grid(row=0, column=0, padx=10, pady=2)

    yellowBtn = Button(btnFrame, width=10, text="Zoom 200", command=zoom200)
    yellowBtn.grid(row=0, column=1, padx=10, pady=2)
 
    greenBtn = Button(btnFrame, width=10, text="Zoom 300", command=zoom300)
    greenBtn.grid(row=0, column=2, padx=10, pady=2)

    greenBtn2 = Button(btnFrame, width=10, text="Zoom 400", command=zoom400)
    greenBtn2.grid(row=0, column=3, padx=10, pady=2)

    greenBtn3 = Button(btnFrame, width=10, text="Zoom 500", command=zoom500)
    greenBtn3.grid(row=0, column=4, padx=10, pady=2)


    ledoffBtn = Button(btnFrame, width=10, text="LED Off", command=ledoff)
    ledoffBtn.grid(row=2,column=1, padx=10, pady=2)

    listcamerasBtn = Button(btnFrame, width=10, text="List Cameras", command=listcameras)
    listcamerasBtn.grid(row=2,column=3, padx=10, pady=2)

    startcameraBtn = Button(btnFrame, width=10, text="Start Camera", command=startcamera)
    startcameraBtn.grid(row=2,column=0, padx=10, pady=2)

    myval = checkexposurestate(0)
    if myval != 'exposure_auto: 3\n':
        mystate = "Auto Exposure:On"
    else:
        mystate = "Auto Exposure:Off"

    myval2 = checkfocusstate(0)
    if myval2 != 'focus_auto: 1\n':
        mystate2 = "Auto Focus:On"
    else:
        mystate2 = "Auto Focus:Off"


    t_btn2 = Button(btnFrame, text=str(mystate2), width=12, command=toggle2)
    t_btn2.grid(row=2,column=4, pady=5)

    t_btn = Button(btnFrame, text=str(mystate), width=12, command=toggle)
    t_btn.grid(row=2,column=2, pady=5)

    w = Scale(root, label="Tilt", from_=-36000,to=36000, resolution=3600, length=340, command=tiltcamera)
    w.grid(row=0,column=0, rowspan=3)

    w = Scale(root, label="Exposure", from_=3,to=2047, resolution=100, length=340, command=adjexposure)
    w.grid(row=0,column=3, rowspan=3)

    # Focus Camera Slider
    w = Scale(root, label="Focus", from_=0,to=250, resolution=1, length=540, orient=HORIZONTAL, command=adjfocus)
    w.grid(row=1,column=1)

    # PAN Camera slider
    w = Scale(root, label="PAN", from_=-36000,to=36000, resolution=3600, length=540, orient=HORIZONTAL, command=pancamera)
    w.grid(row=2,column=1)

    # Adjust Sharpness slider
    w = Scale(root, label="Sharpness", from_=3,to=2047, resolution=100, length=540, orient=HORIZONTAL, command=setsharpness)
    w.grid(row=3,column=1)

    colorLog.delete(1.0,END)
    root.mainloop()
else:
    print ("bye")

