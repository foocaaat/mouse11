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
from multiprocessing import Process
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
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
message = b'test'
addr = ("192.168.1.56", 12000)

while True:
    time.sleep(0.030)
    if key == 0:
        try:
            if keyboard.is_pressed('h') == False and l2 == 1:
                client_socket.sendto(b'2', addr)
                l2=0
            if keyboard.is_pressed('y') == False and r2 == 1:
                client_socket.sendto(b'4', addr)
                r2=0
            if keyboard.is_pressed('u') == False and b2 == 1:
                client_socket.sendto(b'6', addr)
                b2=0
        except:
            pass
        os.system( "setxkbmap &")
        keyboard.wait("capslock")
        os.system( "xkbset mousekeys")
        os.system( "xmodmap " + xmouse)
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
        if keyboard.is_pressed('h') == True and l2 == 0:
            client_socket.sendto(b'1', addr)
            l2=1
        if keyboard.is_pressed('h') == False and l2 == 1:
            client_socket.sendto(b'2', addr)
            l2=0
        if keyboard.is_pressed('y') == True and r2 == 0:
            client_socket.sendto(b'3', addr)
            r2=1
        if keyboard.is_pressed('y') == False and r2 == 1:
            client_socket.sendto(b'4', addr)
            r2=0
        if keyboard.is_pressed('u') == True and b2 == 0:
            client_socket.sendto(b'5', addr)
            b2=1
        if keyboard.is_pressed('u') == False and b2 == 1:
            client_socket.sendto(b'6', addr)
            b2=0

    if keyboard.is_pressed('capslock') == False and key == 1:
        key = 0

