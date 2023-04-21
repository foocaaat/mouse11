import keyboard
import os
from time import sleep
sleep(1)
os.system("xmodmap -e 'keycode 9 ='")
recorded = keyboard.record(until='esc')
os.system("echo | dmenu > .cache/tmpe")
m = int(open('.cache/tmpe', 'r').read())
sleep(1)
for x in range(1, m):
    keyboard.play(recorded)

os.system( "setxkbmap &")
