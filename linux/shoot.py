from pynput.mouse import Button
from action import keypress

from main import keymouse
import time
import sys
#import pyautogui as bot
import mouse


time.sleep(5)
delay=60   
close_time=time.time()+delay

while True:

    keymouse()
    #time.sleep(2)
    #mouse.click(Button.left)

    if time.time()>close_time:
        sys.exit()