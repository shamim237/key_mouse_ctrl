import re
import time
import ctypes

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

                ctypes.windll.user32.keybd_event(0x57, 0, 0, 0) # W Key Down
                time.sleep(2)
                #mouse.move(5, 0)
                ctypes.windll.user32.keybd_event(0x41, 0, 0, 0) # A down
                time.sleep(1)
                ctypes.windll.user32.keybd_event(0x41, 0, 0x0002, 0) # A Up
                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            
            elif fa != 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fd == 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0, 0) # W Key Down
                time.sleep(2)
                #mouse.move(3, 0)
                ctypes.windll.user32.keybd_event(0x44, 0, 0, 0) # D down
                time.sleep(1)
                ctypes.windll.user32.keybd_event(0x44, 0, 0x0002, 0) # D Up
                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            elif fd != 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fs == 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0, 0) # W Key Down
                #time.sleep(2)
                ctypes.windll.user32.SetCursorPos(729, 280)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                #mouse.move(3, 0)
                #bot.press("d") and mouse.click(Button.left, 4)
                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            elif fs != 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if fds == 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0, 0) # W Key Down
                #time.sleep(2)
                ctypes.windll.user32.SetCursorPos(729, 280)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                #mouse.move(15, -15)
                ctypes.windll.user32.keybd_event(0x44, 0, 0, 0) # D down
                time.sleep(2)
                ctypes.windll.user32.keybd_event(0x44, 0, 0x0002, 0) # D Up
                ctypes.windll.user32.SetCursorPos(729, 280)
                ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            elif fds != 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if rld == 0:
                
                ctypes.windll.user32.keybd_event(0x52, 0, 0, 0) # D down
                time.sleep(2)

            elif rld != 0: 

                pass

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
                
            if jump == 0:

                ctypes.windll.user32.keybd_event(0x20, 0, 0, 0) # D down

            elif jump !=0:

                pass

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if f == 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0, 0) # W Key Down
                time.sleep(2)


            elif f != 0:

                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

            if sw == 0:

                ctypes.windll.user32.keybd_event(0x10, 0, 0, 0) # W Key Down
                ctypes.windll.user32.keybd_event(0x57, 0, 0, 0) # W Key Down
                time.sleep(2)
                ctypes.windll.user32.keybd_event(0x57, 0, 0x0002, 0) # W Key Up
                ctypes.windll.user32.keybd_event(0x10, 0, 0x0002, 0) # W Key Up

            elif sw !=0:
                pass

            ctypes.windll.user32.SetCursorPos(729, 280)
            ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
            ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up


time.sleep(5)
keymouse()