#!/usr/bin/python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import keyboard 
import time
from pynput.mouse import Controller,Button
mouse=Controller()

def ax(velocity, pos, neg):
    if (pos == 0 and neg == 0):
        return 0
    if (pos + neg == 0):
        return 0
    return velocity * 0.920 + 1 * (pos + neg)

ee=0
key = 0
VX,VY = 0 ,0
eed=0.010

while True:
    if key == 0:
        keyboard.wait("capslock")
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


        if keyboard.is_pressed("Shift+o") == True and ee == 0:
            if eed == 0.010:
                eed=0.011
            elif eed == 0.011:
                eed=0.020
            elif eed == 0.020:
                eed=0.040
            elif eed == 0.040:
                eed=0.010
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


    if keyboard.is_pressed('capslock') == False and key == 1:
        key = 0
