import re
import time
import pyautogui as bot
from pynput.mouse import Button, Controller
import mouse as ms

mouse = Controller()
bot.FAILSAFE = False

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


            
            mouse.click(Button.left, 4)

            if fa == 0:

                bot.keyDown('w')
                time.sleep(2)
                mouse.move(5, 0)
                bot.press("a") 
                bot.keyUp("w")

            
            elif fa != 0:

                bot.keyUp("w")

            mouse.click(Button.left, 4)

            if fd == 0:

                bot.keyDown('w')
                time.sleep(2)
                mouse.move(3, 0)
                bot.press("d") 
                bot.keyUp("w")

            elif fd != 0:

                bot.keyUp("w")

            mouse.click(Button.left, 4)

            if fs == 0:

                bot.keyDown('w')
                #time.sleep(2)
                mouse.click(Button.left, 4)
                mouse.move(3, 0)
                #bot.press("d") and mouse.click(Button.left, 4)
                #bot.keyUp("w")

            elif fs != 0:

                bot.keyUp("w")

            mouse.click(Button.left, 4)

            if fds == 0:

                bot.keyDown('w')
                #time.sleep(2)
                mouse.click(Button.left, 4)
                #mouse.move(15, -15)
                bot.press("d")
                mouse.click(Button.left, 4)
                bot.keyUp("w")

            elif fds != 0:

                bot.keyUp("w")

            mouse.click(Button.left, 4)

            if rld == 0:
                
                bot.press("r")
                time.sleep(2)

            elif rld != 0: 

                pass

            mouse.click(Button.left, 4)
                
            if jump == 0:

                bot.press("space", presses=1)

            elif jump !=0:

                pass

            mouse.click(Button.left, 4)

            if f == 0:

                bot.keyDown("w")
                time.sleep(2)


            elif f != 0:

                bot.keyUp("w")

            mouse.click(Button.left, 4)

            if sw == 0:

                bot.keyDown("shift")
                bot.keyDown("w")
                time.sleep(2)
                bot.keyUp("w")
                bot.keyUp("shift")

            elif sw !=0:
                pass

            mouse.click(Button.left, 4)

                



# with open("action.txt", "r")  as action:

#     data = action.read()

#     data = re.findall("shoot", data)

#     #d = data.group(0)

#     #print(len(data))