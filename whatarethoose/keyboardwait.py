import keyboard
import math
import os
import time

# A dictionary to store the start time of each key press
key_times = {}

# A set to store the keys that are currently pressed
pressed_keys = set()

# A variable to store the total duration of all the key presses
total_duration = 0

# A variable to store the number of key presses
key_count = 0
wpm = 0
average_duration = 0
output=0

# A callback function to handle key press events
def on_press(event):
    global wpm
    if wpm < 100:
        wpm = math.trunc(min(wpm + math.log10(100 - wpm + 1), 100))
    # Get the name of the key
    key = event.name
    # Get the current time
    now = time.time()
    # Check if the key is already in the set of pressed keys
    if key not in pressed_keys:
        # Add the key to the set of pressed keys
        pressed_keys.add(key)
        # Store the start time of the key press in the dictionary
        key_times[key] = now

# A callback function to handle key release events
def on_release(event):
    # Get the name of the key
    key = event.name
    # Get the current time
    now = time.time()
    if key == "enter":
        return
    # Get the start time of the key press from the dictionary
    start = key_times.get(key, None)
    # If the start time is found, calculate the duration of the key press in milliseconds
    if start is not None:
        duration = (now - start) * 1000
        # Update the total duration and the number of key presses
        global total_duration, key_count
        total_duration += duration
        key_count += 1
        # Calculate the overage duration of all the key presses in milliseconds
        global average_duration
        average_duration=math.trunc(total_duration / key_count)
        # Print the average duration with two decimal places
        # Remove the key from the dictionary
        del key_times[key]
    # Remove the key from the set of pressed keys
    pressed_keys.discard(key)
    if key == "tab":
        print(f"{average_duration:.2f} milliseconds")
        total_duration = 0
        key_count = 0

# Hook the keyboard events with the callback functions
keyboard.hook(on_press)
keyboard.on_release(on_release, suppress=False)

# Wait for the user to press esc to exit
os.system(f"echo {0} > .dis")
second=0
add=0
wpm2=0
while True:
    time.sleep(0.1)
    second+=1
    os.system('clear')
    if wpm2 >= wpm:
        add=math.trunc(add*0.9)
    wpm2=wpm
    wpm=math.trunc(wpm*0.9)
    if second == 10:
        if 10 < wpm < 100:
            add+=6
        if wpm == 0:
            add=0

        second=0
    print(wpm)
    print(add)
    if 1 < wpm < 100:
        output=math.trunc(max(3,math.sin((add+wpm+4)*0.05)*10))
    if wpm < 1:
        output=0
        
    print(output)
    os.system(f"echo {output} > .dis")
    print(average_duration)
    if average_duration * 2 <= 300:
        average_duration=math.trunc(average_duration*2) 
    else:
        average_duration = 300
keyboard.wait("f12")
