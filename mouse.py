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
    if key == 0:
        keyboard.wait("capslock")
        os.system( "xkbset mousekeys")
        if eed == 0.010:
            os.system("echo \>\>\>\> > .cache/mouse &")
        elif eed == 0.011:
            os.system("echo \>\>\> > .cache/mouse &")
        elif eed == 0.020:
            os.system("echo \>\> > .cache/mouse &")
        elif eed == 0.040:
            os.system("echo \> > .cache/mouse &")
        key = 1

    if key == 1: 
        up = - int(keyboard.is_pressed('w') == True)
        left = - int(keyboard.is_pressed('a') == True)
        down = int(keyboard.is_pressed('s') == True)
        right = int(keyboard.is_pressed('d') == True)
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

        if keyboard.is_pressed('o') == False and keyboard.is_pressed('r') == True:
            mouse.scroll(0,1)
            time.sleep(0.01)
        if keyboard.is_pressed('o') == False and keyboard.is_pressed('f') == True:
            mouse.scroll(0,-1)
            time.sleep(0.01)

        if keyboard.is_pressed('o') == True and keyboard.is_pressed('r') == True:
            mouse.scroll(0,1)
            time.sleep(0.1)
        if keyboard.is_pressed('o') == True and keyboard.is_pressed('f') == True:
            mouse.scroll(0,-1)
            time.sleep(0.1)

        if keyboard.is_pressed('o') == False and keyboard.is_pressed('e') == True:
            mouse.scroll(-1,0)
            time.sleep(0.01)
        if keyboard.is_pressed('o') == False and keyboard.is_pressed('t') == True:
            mouse.scroll(1,0)
            time.sleep(0.01)

        if keyboard.is_pressed('o') == True and keyboard.is_pressed('e') == True:
            mouse.scroll(-1,0)
            time.sleep(0.1)
        if keyboard.is_pressed('o') == True and keyboard.is_pressed('t') == True:
            mouse.scroll(1,0)
            time.sleep(0.1)

        if keyboard.is_pressed('h') == True and l2 == 0:
            keyboard2.press(Key.ctrl)
            l2=1
        if keyboard.is_pressed('h') == False and l2 == 1:
            keyboard2.release(Key.ctrl)
            l2=0
        if keyboard.is_pressed('y') == True and r2 == 0:
            keyboard2.press(Key.alt)
            r2=1
        if keyboard.is_pressed('y') == False and r2 == 1:
            keyboard2.release(Key.alt)
            r2=0
        if keyboard.is_pressed('u') == True and b2 == 0:
            keyboard2.press(Key.shift)
            b2=1
        if keyboard.is_pressed('u') == False and b2 == 1:
            keyboard2.release(Key.shift)
            b2=0

        if keyboard.is_pressed('space'):
            if keyboard.is_pressed('1') == True and w1 == 0:
                os.system( "i3 workspace 1")
                w1=1
            if keyboard.is_pressed('1') == False and w1 == 1:
                w1=0

            if keyboard.is_pressed('2') == True and w2 == 0:
                os.system( "i3 workspace 2")
                w2=1
            if keyboard.is_pressed('2') == False and w2 == 1:
                w2=0

            if keyboard.is_pressed('3') == True and w3 == 0:
                os.system( "i3 workspace 3")
                w3=1
            if keyboard.is_pressed('3') == False and w3 == 1:
                w3=0

            if keyboard.is_pressed('4') == True and w4 == 0:
                os.system( "i3 workspace 4")
                w4=1
            if keyboard.is_pressed('4') == False and w4 == 1:
                w4=0

            if keyboard.is_pressed('5') == True and w5 == 0:
                os.system( "i3 workspace 5")
                w5=1
            if keyboard.is_pressed('5') == False and w5 == 1:
                w5=0

            if keyboard.is_pressed('6') == True and w6 == 0:
                os.system( "i3 workspace 6")
                w6=1
            if keyboard.is_pressed('6') == False and w6 == 1:
                w6=0

            if keyboard.is_pressed('7') == True and w7 == 0:
                os.system( "i3 workspace 7")
                w7=1
            if keyboard.is_pressed('7') == False and w7 == 1:
                w7=0

            if keyboard.is_pressed('8') == True and w8 == 0:
                os.system( "i3 workspace 8")
                w8=1
            if keyboard.is_pressed('8') == False and w8 == 1:
                w8=0

            if keyboard.is_pressed('9') == True and w9 == 0:
                os.system( "i3 workspace 9")
                w9=1
            if keyboard.is_pressed('9') == False and w9 == 1:
                w9=0

            if keyboard.is_pressed('0') == True and w10 == 0:
                os.system( "i3 workspace 10")
                w10=1
            if keyboard.is_pressed('0') == False and w10 == 1:
                w10=0

            if keyboard.is_pressed('-') == True and w11 == 0:
                os.system( "i3 workspace 11")
                w11=1
            if keyboard.is_pressed('-') == False and w11 == 1:
                w11=0

            if keyboard.is_pressed('=') == True and w12 == 0:
                os.system( "i3 workspace 12")
                w12=1
            if keyboard.is_pressed('=') == False and w12 == 1:
                w12=0

    if keyboard.is_pressed('capslock') == False and key == 1:
        os.system( "xkbset -mousekeys &")
        os.system( "setxkbmap &")
        keyboard2.release(Key.ctrl)
        keyboard2.release(Key.alt)
        keyboard2.release(Key.shift)
 #      os.system( "xdotool keyup u && xdotool keyup y && xdotool keyup h && xdotool keyup o & ")
        os.system("echo > .cache/mouse &")
        key = 0

