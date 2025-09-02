import time
import pyautogui


while True:
        time.sleep(0.5)
        try:
            location = pyautogui.locateOnScreen(fr'd:\python\msm\coletor\cold.png')
            print('image found')
            pyautogui.leftClick(pyautogui.center(location))
            break
        except pyautogui.ImageNotFoundException:
            print('ImageNocold')