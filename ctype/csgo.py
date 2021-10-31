import re
import time
import ctypes
from cp1 import MOUSEINPUT, KEYBDINPUT, ReleaseKey, PressKey, HARDWAREINPUT, INPUT

KEY_A = 0x41
KEY_B = 0x42
KEY_D = 0x44
KEY_R = 0x52
KEY_S = 0x53
KEY_W = 0x57
SPACE = 0x20 
SHIFT = 0x10  


def keymouse():


    with open("action.txt", "r")  as action:

        data = action.readlines()

        for datas in data:

            fa = datas.find("hld_w+a")

            fd = datas.find("hld_w+d")

            fds = datas.find("hld_w+d+shoot")

            fs = datas.find("hld_w+shoot")

            rld = datas.find("r")

            f = datas.find("hld_w")

            jump = datas.find("space")

            #sw = datas.find("space+hld_w")

            sw= datas.find("hld_shift+hld_w")


            
            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fa == 0:

                PressKey(KEY_W)
                time.sleep(2)
                #mouse.move(5, 0)
                PressKey(KEY_W) # A down
                time.sleep(1)
                ReleaseKey(KEY_W) # A Up
                ReleaseKey(KEY_W) # W Key Up

            
            elif fa != 0:

                ReleaseKey(KEY_W) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fd == 0:

                PressKey(KEY_W) # W Key Down
                time.sleep(2)
                #mouse.move(3, 0)
                PressKey(KEY_D)# D down
                time.sleep(1)
                ReleaseKey(KEY_D) # D Up
                ReleaseKey(KEY_W) # W Key Up

            elif fd != 0:

                ReleaseKey(KEY_W)# W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fs == 0:

                PressKey(KEY_W) # W Key Down
                #time.sleep(2)
                ctypes.windll.user32.SetCursorPos(729, 280)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                #mouse.move(3, 0)
                #bot.press("d") and mouse.click(Button.left, 4)
                ReleaseKey(KEY_W) # W Key Up

            elif fs != 0:

                ReleaseKey(KEY_W) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fds == 0:

                PressKey(KEY_W) # W Key Down
                #time.sleep(2)
                ctypes.windll.user32.SetCursorPos(729, 280)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                #mouse.move(15, -15)
                PressKey(KEY_D) # D down
                time.sleep(2)
                ReleaseKey(KEY_D) # D Up
                ctypes.windll.user32.SetCursorPos(729, 280)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                ReleaseKey(KEY_W)# W Key Up

            elif fds != 0:

                ReleaseKey(KEY_W) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if rld == 0:
                
                PressKey(KEY_R) # R down
                time.sleep(2)

            elif rld != 0: 

                pass

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                
            if jump == 0:

                PressKey(SPACE)

            elif jump !=0:

                pass

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if f == 0:

                PressKey(KEY_W) # W Key Down
                time.sleep(2)


            elif f != 0:

                ReleaseKey(KEY_W) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if sw == 0:

                PressKey(SHIFT) # shift Key Down
                PressKey(KEY_W) # W Key Down
                time.sleep(2)
                ReleaseKey(SHIFT) # SHIFT Key Up
                ReleaseKey(KEY_W) # W Key Up

            elif sw !=0:
                
                pass

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up


time.sleep(5)
keymouse()