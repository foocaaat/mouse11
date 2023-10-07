#!/usr/bin/python3
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
xmod = os.path.join(script_dir, "xmods")
mose = os.path.join(script_dir, "mose.sh")
import keyboard 
import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
s9=0
s10=0
s11=0
s12=0
s13=0
s14=0
s15=0
s16=0
s17=0
s18=0
s19=0
s20=0
s21=0
s22=0
s23=0
s24=0
s25=0
s26=0
s27=0
s28=0
s29=0
s30=0
s31=0
s32=0
s33=0
s34=0
s35=0
s36=0
s37=0
s38=0
s39=0
s40=0
s41=0
s42=0
s43=0
s44=0
s45=0
s46=0
s47=0
s48=0
s49=0
s50=0
s51=0
s52=0
s53=0
s54=0
s55=0
s56=0
s57=0
s58=0
s59=0
s60=0
s61=0
s62=0
s63=0
s64=0
s65=0
s66=0
s67=0

while True:
    time.sleep(0.003)
    ser.write(bytes([1]))
    ser.write(bytes([2]))
