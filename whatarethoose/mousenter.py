#!/usr/bin/python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
xmod = os.path.join(script_dir, "xmods")
mose = os.path.join(script_dir, "mose.sh")
import keyboard 
import time
import mouse
from pynput.keyboard import Key, Controller
keyboard2 = Controller()
from pynput.mouse import Controller,Button
mouse=Controller()

def ax(velocity, pos, neg):
    if (pos == 0 and neg == 0):
        return 0
    if (pos + neg == 0):
        return 0
    return velocity * 0.920 + 1 * (pos + neg)

eed=0.010


e2=0
r2=0
l2=0
l3=0
l4=0
b2=0
ee=0
bkey=0
xkey=0
bey=0
xey=0
l=0
key = 0
VX,VY = 0 ,0
windows = 0
xmouse = os.path.join(script_dir, ".Xmouse")
windows = 0

w1=0
w2=0
w3=0
w4=0
w5=0
w6=0
w7=0
w8=0
w9=0
w10=0
w11=0
w12=0




while True:
        up = - int(keyboard.is_pressed('p') == True)
        left = - int(keyboard.is_pressed('l') == True)
        down = int(keyboard.is_pressed(';') == True)
        right = int(keyboard.is_pressed('apostrophe') == True)
        VX = ax(VX, left, right)
        VY = ax(VY, up, down)
        if (VY + VX != 0 ):
      	    mouse.move(VX,VY)
#           os.system("xdotool mousemove_relative -- {} {} &".format(VX, VY))


        if keyboard.is_pressed("Shift+o") == True and ee == 0:
            if eed == 0.010:
                eed=0.011
                os.system("echo \>\>\> > .cache/mouse &")
                os.system("pkill mose.sh &")
            elif eed == 0.011:
                eed=0.020
                os.system("echo  \>\> > .cache/mouse &")
            elif eed == 0.020:
                eed=0.040
                os.system("echo \> > .cache/mouse &")
            elif eed == 0.040:
                eed=0.010
                os.system("echo \>\>\>\> > .cache/mouse &")
                os.system(f"{mose} &")
            ee=1
        if keyboard.is_pressed("o") == False and ee == 1:
            ee=0
        if keyboard.is_pressed("o") == True:
            time.sleep(0.030)
        else:
            time.sleep(eed)


