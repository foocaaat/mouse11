#!/usr/bin/python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import keyboard 
import time
import mouse

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

a1=0
w1=0
s1=0
e1=0
d1=0
f1=0
t1=0
g1=0
y1=0
h1=0
u1=0
j1=0
k1=0



while True:
    if keyboard.is_pressed('a') == True and a1 == 0:
        os.system("echo 1 > yeaa")
        a1=1
    if keyboard.is_pressed('a') == False and a1 == 1:
        os.system("echo 0 > yeaa")
        a1=0

    if keyboard.is_pressed('w') == True and w1 == 0:
        os.system("echo 1 > yeaw")
        w1=1
    if keyboard.is_pressed('w') == False and w1 == 1:
        os.system("echo 0 > yeaw")
        w1=0

    if keyboard.is_pressed('s') == True and s1 == 0:
        os.system("echo 1 > yeas")
        s1=1
    if keyboard.is_pressed('s') == False and s1 == 1:
        os.system("echo 0 > yeas")
        s1=0

    if keyboard.is_pressed('e') == True and e1 == 0:
        os.system("echo 1 > yeae")
        e1=1
    if keyboard.is_pressed('e') == False and e1 == 1:
        os.system("echo 0 > yeae")
        e1=0

    if keyboard.is_pressed('d') == True and d1 == 0:
        os.system("echo 1 > yead")
        d1=1
    if keyboard.is_pressed('d') == False and d1 == 1:
        os.system("echo 0 > yead")
        d1=0

    if keyboard.is_pressed('f') == True and f1 == 0:
        os.system("echo 1 > yeaf")
        f1=1
    if keyboard.is_pressed('f') == False and f1 == 1:
        os.system("echo 0 > yeaf")
        f1=0

    if keyboard.is_pressed('t') == True and t1 == 0:
        os.system("echo 1 > yeat")
        t1=1
    if keyboard.is_pressed('t') == False and t1 == 1:
        os.system("echo 0 > yeat")
        t1=0

    if keyboard.is_pressed('g') == True and g1 == 0:
        os.system("echo 1 > yeag")
        g1=1
    if keyboard.is_pressed('g') == False and g1 == 1:
        os.system("echo 0 > yeag")
        g1=0

    if keyboard.is_pressed('y') == True and y1 == 0:
        os.system("echo 1 > yeay")
        y1=1
    if keyboard.is_pressed('y') == False and y1 == 1:
        os.system("echo 0 > yeay")
        y1=0

    if keyboard.is_pressed('h') == True and h1 == 0:
        os.system("echo 1 > yeah")
        h1=1
    if keyboard.is_pressed('h') == False and h1 == 1:
        os.system("echo 0 > yeah")
        h1=0

    if keyboard.is_pressed('u') == True and u1 == 0:
        os.system("echo 1 > yeau")
        u1=1
    if keyboard.is_pressed('u') == False and u1 == 1:
        os.system("echo 0 > yeau")
        u1=0

    if keyboard.is_pressed('j') == True and j1 == 0:
        os.system("echo 1 > yeaj")
        j1=1
    if keyboard.is_pressed('j') == False and j1 == 1:
        os.system("echo 0 > yeaj")
        j1=0

    if keyboard.is_pressed('k') == True and k1 == 0:
        os.system("echo 1 > yeak")
        k1=1
    if keyboard.is_pressed('k') == False and k1 == 1:
        os.system("echo 0 > yeak")
        k1=0

    time.sleep(0.030)


