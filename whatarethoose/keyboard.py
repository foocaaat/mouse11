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
    if keyboard.is_pressed(41) and s1==0: ser.write(bytes([1])); s1=1 
    elif not keyboard.is_pressed(41) and s1==1: ser.write(bytes([2])); s1=0
    if keyboard.is_pressed('1') and s2==0: ser.write(bytes([3])); s2=1 
    elif not keyboard.is_pressed('1') and s2==1: ser.write(bytes([4])); s2=0
    if keyboard.is_pressed('2') and s3==0: ser.write(bytes([5])); s3=1 
    elif not keyboard.is_pressed('2') and s3==1: ser.write(bytes([6])); s3=0
    if keyboard.is_pressed('3') and s4==0: ser.write(bytes([7])); s4=1 
    elif not keyboard.is_pressed('3') and s4==1: ser.write(bytes([8])); s4=0
    if keyboard.is_pressed('4') and s5==0: ser.write(bytes([9])); s5=1 
    elif not keyboard.is_pressed('4') and s5==1: ser.write(bytes([10])); s5=0
    if keyboard.is_pressed('5') and s6==0: ser.write(bytes([11])); s6=1 
    elif not keyboard.is_pressed('5') and s6==1: ser.write(bytes([12])); s6=0
    if keyboard.is_pressed('6') and s7==0: ser.write(bytes([13])); s7=1 
    elif not keyboard.is_pressed('6') and s7==1: ser.write(bytes([14])); s7=0
    if keyboard.is_pressed('7') and s8==0: ser.write(bytes([15])); s8=1 
    elif not keyboard.is_pressed('7') and s8==1: ser.write(bytes([16])); s8=0
    if keyboard.is_pressed('8') and s9==0: ser.write(bytes([17])); s9=1 
    elif not keyboard.is_pressed('8') and s9==1: ser.write(bytes([18])); s9=0
    if keyboard.is_pressed('9') and s10==0: ser.write(bytes([19])); s10=1 
    elif not keyboard.is_pressed('9') and s10==1: ser.write(bytes([20])); s10=0
    if keyboard.is_pressed('0') and s11==0: ser.write(bytes([21])); s11=1 
    elif not keyboard.is_pressed('0') and s11==1: ser.write(bytes([22])); s11=0
    if keyboard.is_pressed('minus') and s12==0: ser.write(bytes([23])); s12=1 
    elif not keyboard.is_pressed('minus') and s12==1: ser.write(bytes([24])); s12=0
    if keyboard.is_pressed('=') and s13==0: ser.write(bytes([25])); s13=1 
    elif not keyboard.is_pressed('=') and s13==1: ser.write(bytes([26])); s13=0
    if keyboard.is_pressed(14) == True and s14==0: ser.write(bytes([27])); s14=1 
    if keyboard.is_pressed(14) == False and s14==1: ser.write(bytes([28])); s14=0
    if keyboard.is_pressed(15) == True and s15==0: ser.write(bytes([29])); s15=1 
    if keyboard.is_pressed(15) == False and s15==1: ser.write(bytes([30])); s15=0
    if keyboard.is_pressed('q') and s16==0: ser.write(bytes([31])); s16=1 
    elif not keyboard.is_pressed('q') and s16==1: ser.write(bytes([32])); s16=0
    if keyboard.is_pressed('w') and s17==0: ser.write(bytes([33])); s17=1 
    elif not keyboard.is_pressed('w') and s17==1: ser.write(bytes([34])); s17=0
    if keyboard.is_pressed('e') and s18==0: ser.write(bytes([35])); s18=1 
    elif not keyboard.is_pressed('e') and s18==1: ser.write(bytes([36])); s18=0
    if keyboard.is_pressed('r') and s19==0: ser.write(bytes([37])); s19=1 
    elif not keyboard.is_pressed('r') and s19==1: ser.write(bytes([38])); s19=0
    if keyboard.is_pressed('t') and s20==0: ser.write(bytes([39])); s20=1 
    elif not keyboard.is_pressed('t') and s20==1: ser.write(bytes([40])); s20=0
    if keyboard.is_pressed('y') and s21==0: ser.write(bytes([41])); s21=1 
    elif not keyboard.is_pressed('y') and s21==1: ser.write(bytes([42])); s21=0
    if keyboard.is_pressed('u') and s22==0: ser.write(bytes([43])); s22=1 
    elif not keyboard.is_pressed('u') and s22==1: ser.write(bytes([44])); s22=0
    if keyboard.is_pressed(23) == True and s23==0: ser.write(bytes([45])); s23=1 
    if keyboard.is_pressed(23) == False and s23==1: ser.write(bytes([46])); s23=0
    if keyboard.is_pressed('o') and s24==0: ser.write(bytes([47])); s24=1 
    elif not keyboard.is_pressed('o') and s24==1: ser.write(bytes([48])); s24=0
    if keyboard.is_pressed('p') and s25==0: ser.write(bytes([49])); s25=1 
    elif not keyboard.is_pressed('p') and s25==1: ser.write(bytes([50])); s25=0
    if keyboard.is_pressed('[') and s26==0: ser.write(bytes([51])); s26=1 
    elif not keyboard.is_pressed('[') and s26==1: ser.write(bytes([52])); s26=0
    if keyboard.is_pressed(']') and s27==0: ser.write(bytes([53])); s27=1 
    elif not keyboard.is_pressed(']') and s27==1: ser.write(bytes([54])); s27=0
    if keyboard.is_pressed('\\') and s28==0: ser.write(bytes([55])); s28=1 
    elif not keyboard.is_pressed('\\') and s28==1: ser.write(bytes([56])); s28=0
    if keyboard.is_pressed('caps lock') and s29==0: ser.write(bytes([57])); s29=1 
    elif not keyboard.is_pressed('caps lock') and s29==1: ser.write(bytes([58])); s29=0
    if keyboard.is_pressed('a') and s30==0: ser.write(bytes([59])); s30=1 
    elif not keyboard.is_pressed('a') and s30==1: ser.write(bytes([60])); s30=0
    if keyboard.is_pressed('s') and s31==0: ser.write(bytes([61])); s31=1 
    elif not keyboard.is_pressed('s') and s31==1: ser.write(bytes([62])); s31=0
    if keyboard.is_pressed('d') and s32==0: ser.write(bytes([63])); s32=1 
    elif not keyboard.is_pressed('d') and s32==1: ser.write(bytes([64])); s32=0
    if keyboard.is_pressed('f') and s33==0: ser.write(bytes([65])); s33=1 
    elif not keyboard.is_pressed('f') and s33==1: ser.write(bytes([66])); s33=0
    if keyboard.is_pressed('g') and s34==0: ser.write(bytes([67])); s34=1 
    elif not keyboard.is_pressed('g') and s34==1: ser.write(bytes([68])); s34=0
    if keyboard.is_pressed(35) == True and s35==0: ser.write(bytes([69])); s35=1 
    if keyboard.is_pressed(35) == False and s35==1: ser.write(bytes([70])); s35=0
    if keyboard.is_pressed(36) == True and s36==0: ser.write(bytes([71])); s36=1 
    if keyboard.is_pressed(36) == False and s36==1: ser.write(bytes([72])); s36=0
    if keyboard.is_pressed('k') and s37==0: ser.write(bytes([73])); s37=1 
    elif not keyboard.is_pressed('k') and s37==1: ser.write(bytes([74])); s37=0
    if keyboard.is_pressed('l') and s38==0: ser.write(bytes([75])); s38=1 
    elif not keyboard.is_pressed('l') and s38==1: ser.write(bytes([76])); s38=0
    if keyboard.is_pressed(';') and s39==0: ser.write(bytes([77])); s39=1 
    elif not keyboard.is_pressed(';') and s39==1: ser.write(bytes([78])); s39=0
    if keyboard.is_pressed('\'') and s40==0: ser.write(bytes([79])); s40=1 
    elif not keyboard.is_pressed('\'') and s40==1: ser.write(bytes([80])); s40=0
    if keyboard.is_pressed(28) == True and s41==0: ser.write(bytes([81])); s41=1 
    if keyboard.is_pressed(28) == False and s41==1: ser.write(bytes([82])); s41=0
    if keyboard.is_pressed(42) and s42==0: ser.write(bytes([83])); s42=1 
    elif not keyboard.is_pressed(42) and s42==1: ser.write(bytes([84])); s42=0
    if keyboard.is_pressed('z') and s43==0: ser.write(bytes([85])); s43=1 
    elif not keyboard.is_pressed('z') and s43==1: ser.write(bytes([86])); s43=0
    if keyboard.is_pressed('x') and s44==0: ser.write(bytes([87])); s44=1 
    elif not keyboard.is_pressed('x') and s44==1: ser.write(bytes([88])); s44=0
    if keyboard.is_pressed('c') and s45==0: ser.write(bytes([89])); s45=1 
    elif not keyboard.is_pressed('c') and s45==1: ser.write(bytes([90])); s45=0
    if keyboard.is_pressed('v') and s46==0: ser.write(bytes([91])); s46=1 
    elif not keyboard.is_pressed('v') and s46==1: ser.write(bytes([92])); s46=0
    if keyboard.is_pressed('b') and s47==0: ser.write(bytes([93])); s47=1 
    elif not keyboard.is_pressed('b') and s47==1: ser.write(bytes([94])); s47=0
    if keyboard.is_pressed('n') and s48==0: ser.write(bytes([95])); s48=1 
    elif not keyboard.is_pressed('n') and s48==1: ser.write(bytes([96])); s48=0
    if keyboard.is_pressed('m') and s49==0: ser.write(bytes([97])); s49=1 
    elif not keyboard.is_pressed('m') and s49==1: ser.write(bytes([98])); s49=0
    if keyboard.is_pressed(',') and s50==0: ser.write(bytes([99])); s50=1 
    elif not keyboard.is_pressed(',') and s50==1: ser.write(bytes([100])); s50=0
    if keyboard.is_pressed('.') and s51==0: ser.write(bytes([101])); s51=1 
    elif not keyboard.is_pressed('.') and s51==1: ser.write(bytes([102])); s51=0
    if keyboard.is_pressed('/') and s52==0: ser.write(bytes([103])); s52=1 
    elif not keyboard.is_pressed('/') and s52==1: ser.write(bytes([104])); s52=0
    if keyboard.is_pressed(54) and s53==0: ser.write(bytes([105])); s53=1 
    elif not keyboard.is_pressed(54) and s53==1: ser.write(bytes([106])); s53=0
    if keyboard.is_pressed(29) and s54==0: ser.write(bytes([107])); s54=1 
    elif not keyboard.is_pressed(29) and s54==1: ser.write(bytes([108])); s54=0
    if keyboard.is_pressed(125) and s55==0: ser.write(bytes([109])); s55=1 
    elif not keyboard.is_pressed(125) and s55==1: ser.write(bytes([110])); s55=0
    if keyboard.is_pressed(56) and s56==0: ser.write(bytes([111])); s56=1 
    elif not keyboard.is_pressed(56) and s56==1: ser.write(bytes([112])); s56=0
    if keyboard.is_pressed(' ') and s57==0: ser.write(bytes([113])); s57=1 
    elif not keyboard.is_pressed(' ') and s57==1: ser.write(bytes([114])); s57=0
    if keyboard.is_pressed(100) and s58==0: ser.write(bytes([115])); s58=1 
    elif not keyboard.is_pressed(100) and s58==1: ser.write(bytes([116])); s58=0
    if keyboard.is_pressed(97) and s59==0: ser.write(bytes([117])); s59=1 
    elif not keyboard.is_pressed(97) and s59==1: ser.write(bytes([118])); s59=0
    if keyboard.is_pressed('left') and s60==0: ser.write(bytes([119])); s60=1 
    elif not keyboard.is_pressed('left') and s60==1: ser.write(bytes([120])); s60=0
    if keyboard.is_pressed('up') and s61==0: ser.write(bytes([121])); s61=1 
    elif not keyboard.is_pressed('up') and s61==1: ser.write(bytes([122])); s61=0
    if keyboard.is_pressed('down') and s62==0: ser.write(bytes([123])); s62=1 
    elif not keyboard.is_pressed('down') and s62==1: ser.write(bytes([124])); s62=0
    if keyboard.is_pressed('right') and s63==0: ser.write(bytes([125])); s63=1 
    elif not keyboard.is_pressed('right') and s63==1: ser.write(bytes([126])); s63=0
