#!/usr/bin/python3

import keyboard 
import time
import subprocess
import os
from multiprocessing import Process
#from pynput.mouse import Controller,Button
#mouse=Controller()

def ax(velocity, pos, neg):
    if (pos == 0 and neg == 0):
        return 0
    if (pos + neg == 0):
        return 0
    return velocity * 0.982 + 1 * (pos + neg)




def loop_a():
    VX,VY = 0 ,0
    key = 0
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
#          	    mouse.move(VX,VY)
                os.system("xdotool mousemove_relative -- {} {} &".format(VX, VY))

            time.sleep(0.010)
        if keyboard.is_pressed('capslock') == False and key == 1:
            key = 0

def loop_b():
    e=0
    r=0
    l=0
    b=0
    key = 0
    while True:
        if key == 0:
            keyboard.wait("capslock")
            os.system( "xkbset mousekeys")
            key = 1

        if key == 1: 
            if keyboard.is_pressed('o') == False and keyboard.is_pressed('r') == True:
                os.system( "xdotool click --repeat 1 --delay 10 4")
            if keyboard.is_pressed('o') == False and keyboard.is_pressed('f') == True:
                os.system( "xdotool click --repeat 1 --delay 10 5")

            if keyboard.is_pressed('o') == True and keyboard.is_pressed('r') == True:
                os.system( "xdotool click 4")
            if keyboard.is_pressed('o') == True and keyboard.is_pressed('f') == True:
                os.system( "xdotool click 5")

 #           if keyboard.is_pressed('space') == True and l == 0:
 #               os.system( "xdotool mousedown 1")
 #               l=1
 #           if keyboard.is_pressed('space') == False and l == 1:
 #               os.system( "xdotool mouseup 1")
 #               l=0
 #           if keyboard.is_pressed('c') == True and r == 0:
 #               os.system( "xdotool mousedown 3")
 #               r=1
 #           if keyboard.is_pressed('c') == False and r == 1:
 #               os.system( "xdotool mouseup 3")
 #               r=0
            if keyboard.is_pressed('m') == True and b == 0:
                os.system( "xdotool mousedown 2")
                b=1
            if keyboard.is_pressed('m') == False and b == 1:
                os.system( "xdotool mouseup 2")
                b=0
        if keyboard.is_pressed('capslock') == False and key == 1:
            os.system( "xkbset -mousekeys")
            key = 0



def loop_c():
    e2=0
    r2=0
    l2=0
    b2=0
    key = 0
    while True:
        if key == 0:
            keyboard.wait("capslock")
            key = 1

        if key == 1: 
            if keyboard.is_pressed('h') == True and l2 == 0:
                os.system( "xdotool keydown ctrl")
                l2=1
            if keyboard.is_pressed('h') == False and l2 == 1:
                os.system( "xdotool keyup ctrl")
                l2=0
            if keyboard.is_pressed('y') == True and r2 == 0:
                os.system( "xdotool keydown alt")
                r2=1
            if keyboard.is_pressed('y') == False and r2 == 1:
                os.system( "xdotool keyup alt")
                r2=0
            if keyboard.is_pressed('u') == True and b2 == 0:
                os.system( "xdotool keydown shift")
                b2=1
            if keyboard.is_pressed('u') == False and b2 == 1:
                os.system( "xdotool keyup shift")
                b2=0
        if keyboard.is_pressed('capslock') == False and key == 1:
            key = 0


if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
    Process(target=loop_c).start()

