import win32api
import win32gui
import win32con
import win32ui
import random

from screenshot import *
from getUIposition import *

hwnd = setHwnd()
topleftx, toplefty, bottomrightx, bottomrighty = GetXY(hwnd)
print(topleftx, toplefty, bottomrightx, bottomrighty)
width = bottomrightx - topleftx
high = bottomrighty - toplefty
print(width, high)

screenTopLeftX, screenTopLeftY, screenBottomRightX, screenBottomRightY = 55, 78, 405, 709

picScreenLocation = (screenTopLeftX, screenTopLeftY, screenBottomRightX, screenBottomRightY)
hwndScreenLocation = (topleftx, toplefty, bottomrightx, bottomrighty)

def set_cutlocation(picScreenLocation, hwndScreenLocation):
    (hwndTopLeftX, hwndTopLeftY, hwndBottomRightX, hwndBottomRightY) = hwndScreenLocation
    (screenTopLeftX, screenTopLeftY, screenBottomRightX, screenBottomRightY) = picScreenLocation

    cutLocation = ((screenTopLeftX - hwndTopLeftX), 
                   (screenTopLeftY - hwndTopLeftY), 
                   (screenBottomRightX - hwndBottomRightX),
                   (screenBottomRightY - hwndBottomRightY))

    print(cutLocation)
    return cutLocation

#set_cutlocation(picScreenLocation, hwndScreenLocation)
def set_random():
    randomX = (random.random() - 0.5) * 16 #产生[-8, 8]的随机数
    randomY = (random.random() - 0.5) * 16
    randomX = round(randomX) #四舍五入
    randomX = int(randomX)
    randomY = round(randomY)
    randomY = int(randomY)
    return randomX, randomY


def test():
    for num in range(10):
        randomX, randomY = set_random()
        name = './pic/startmovation_' + str(num) + '.png'
        window_capture(1572 + randomX, 859 + randomY, 1859 + randomX, 908 + randomY, filename = name, hwnd = hwnd)

test()





