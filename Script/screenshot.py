###截图
import cv2
import re
from PIL import ImageGrab

def ImageShot(topleftx, toplefty, lowrightx, lowrighty, name):
    piclocation = (topleftx, toplefty, lowrightx, lowrighty)
    im = ImageGrab.grab(piclocation)
    name = re.sub('.png', '', name)
    name = re.sub('.PNG', '', name)
    name = re.sub('.jpg', '', name)
    name = re.sub('.JPG', '', name)
    name = re.sub('.jpeg', '', name)
    name = re.sub('.JPEG', '', name)
    name = re.sub('.tif', '', name)
    name = re.sub('.TIF', '', name)
    count = 0
    im.save(name + '_' + str(count) + '.png')
    return 0

#cutImage(0, 0, 1920, 1080, 'test.png')
 
# 去除字符串中相同的字符
#s = '\tabc\t123\tisk'
#print(s.replace('\t', ''))
#import re
# 去除\r\n\t字符
#s = '\r\nabc\t123\nxyz'
#print(re.sub('[\r\n\t]', '', s))

import time
import win32gui, win32ui, win32con, win32api
def window_capture(leftx, lefty, bottomx, bottomy, filename, hwnd = 0):#截取该窗体的图片
    #该函数在windows界面有所放大的情况下无法使用


# 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, (bottomx - leftx), (bottomy - lefty))
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取该窗体的从左上角（0，0）长宽为（(bottomx - leftx)，(bottomy - lefty)）的图片
    saveDC.BitBlt((0, 0), ((bottomx - leftx), (bottomy - lefty)), mfcDC, (leftx, lefty), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

def getMoniterResolution(MoniterDevNum): #MoniterDevNum是显示器编号
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    #print(MoniterDev) #打印显示器信息
    MoniterWidth = MoniterDev[MoniterDevNum][2][2] #显示器分辨率的宽度
    MoniterHigh = MoniterDev[MoniterDevNum][2][3] #显示器分辨率的高度
    #print (MoniterWidth,MoniterHigh)
    return MoniterWidth, MoniterHigh

#beg = time.time()
#window_capture("./pic/haha.jpg", 0, 1)
#end = time.time()
#print(end - beg)






