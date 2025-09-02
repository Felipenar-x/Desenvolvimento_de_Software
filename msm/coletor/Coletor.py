import pyautogui
import time
import cv2
import numpy as np
import pytesseract
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def diamante():
    while True:
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        location_img = cv2.imread(r'd:\python\msm\coletor\FOTOS\dima.png', cv2.IMREAD_COLOR)
        h, w = location_img.shape[:2]
        result = cv2.matchTemplate(frame, location_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.9:
            x, y = max_loc
            print('dima achado')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            pyautogui.click(x + w//2, y + h//2)
            break
        else:
            print('dima nao achado')


def mapa():
    while True:
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        location_img = cv2.imread(r'd:\python\msm\coletor\FOTOS\mapa.png', cv2.IMREAD_COLOR)
        h, w = location_img.shape[:2]
        result = cv2.matchTemplate(frame, location_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            x, y = max_loc
            print('mapa achado')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            pyautogui.click(x + w//2, y + h//2)
            break
        else:
            print('Mapa nao achado')



def local(x):
    while True:
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        texto = pytesseract.image_to_string(screenshot, lang='por')
        print(texto)


        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        location_img = cv2.imread(fr'd:\python\msm\coletor\FOTOS\{x}.png', cv2.IMREAD_COLOR)
        h, w = location_img.shape[:2]
        result = cv2.matchTemplate(frame, location_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            x0, y0 = max_loc
            print('local achado')
            cv2.rectangle(frame, (x0, y0), (x0 + w, y0 + h), (0, 255, 0), 2)
            pyautogui.click(x0 + w//2, y0 + h//2)
            break
        else:
            print(f'Sem {x}')


def go():
    while True:
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        location_img = cv2.imread(fr'd:\python\msm\coletor\FOTOS\go.png', cv2.IMREAD_COLOR)
        h, w = location_img.shape[:2]
        result = cv2.matchTemplate(frame, location_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            x0, y0 = max_loc
            print('found')
            cv2.rectangle(frame, (x0, y0), (x0 + w, y0 + h), (0, 255, 0), 2)
            pyautogui.click(x0 + w//2, y0 + h//2)
            break
        else:
            print('Sem go')


def normal(x):
    mapa()
    local(x)
    go()
    diamante()


normal('cold')
normal('air')
normal('water')
normal('earth')
normal('shugabush')
normal('EI')
normal('EW')
normal('FH')
normal('FO')
normal('LI')
normal('PI')
normal('FI')
normal('BI')
normal('MS')
normal('cold')
normal('air')
normal('water')
normal('earth')