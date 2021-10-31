import pyautogui as bot
from pynput.mouse import Button, Controller
import time
import re

mouse = Controller()

def keypress():



    with open("log.txt", "r")  as action:

        data = action.readlines()

        for datas in data:

            forward = datas.find("w")

            backward = datas.find("s")

            right = datas.find("d")

            left = datas.find("a")


            if forward == 0:

                bot.keyDown("w")
                time.sleep(1)
                mouse.click(Button.left, 10)
                bot.press("r", interval=10)
                bot.keyUp("w")
                time.sleep(1)

            elif forward !=0:

                bot.keyUp("w")
        

            if backward == 0:

                bot.keyDown("s")
            
            elif backward != 0:
                
                bot.keyUp("s")

            if right == 0:

                bot.keyDown("d")

            elif right != 0:
                
                bot.keyUp("d")    

            if left == 0:

                bot.keyDown("a")    

            elif left != 0:
                
                bot.keyUp("a")



