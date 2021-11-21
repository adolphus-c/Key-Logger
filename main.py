import pynput

from pynput.keyboard import Key, Listener

count = 0 
keys = []

def on_press(key):
    print("{0} pressed".format(key))
    
def write
    
def on_release(key):
    if key == Key.esc:
        return 0

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()