#!/usr/bin/python3
from pynput import keyboard
from time import sleep
import os

valid_keys = set()
valid_keys.update(set("abcdefghijklmnopqrstuvwxyz"))
valid_keys.update(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
valid_keys.update(set("~!@#$%^&*()_+-={}|[]:<>?,./"))

def on_press(key):
    global combination
    try:
        if key == keyboard.Key.tab or key == keyboard.Key.alt or key == keyboard.Key.cmd or key == keyboard.Key.space or key == keyboard.Key.ctrl or key == keyboard.Key.enter:
            combination = ""
            os.system(f"echo {combination}  > .cache/combi")
        elif key == keyboard.Key.backspace:
            if combination != "":
                combination = combination[:-1]
                os.system(f"echo '{combination}'  > .cache/combi")
        elif key.char in valid_keys:
            combination = combination + key.char
            os.system(f"echo '{combination}'  > .cache/combi")
    except:
        pass

def on_release(key):
    try:
        if key.char not in valid_keys and key != keyboard.Key.backspace:
            global combination
            combination = ""
            os.system(f"echo {combination}  > .cache/combi")
    except:
        pass
    if key == keyboard.Key.tab or key == keyboard.Key.alt or key == keyboard.Key.cmd or key == keyboard.Key.space or key == keyboard.Key.ctrl or key == keyboard.Key.enter:
        combination = ""
        os.system(f"echo {combination}  > .cache/combi")

while True:
    sleep(1)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
