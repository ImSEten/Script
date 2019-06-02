import win32gui
import win32api
import win32con

def GetXY(hwnd, print_bug = True): #获得模拟器的窗口位置
    if print_bug == True:
        print('hwnd=',hwnd)
    text = win32gui.GetWindowText(hwnd)                      #返回的是窗口的名字（不一定是窗口左上角显示的名字）
    if print_bug == True:
        print('操作的窗口名为：',text)
    topleftx, toplefty, bottomrightx, bottomrighty = win32gui.GetWindowRect(hwnd)  #(left,top)是左上角的坐标，(right,bottom)是右下角的坐标
    #win32gui.SetForegroundWindow(hwnd)
    return topleftx, toplefty, bottomrightx, bottomrighty #返回模拟器的左上角(x,y)坐标（即left,top），以及模拟器窗口的句柄

def setHwnd():
    hwnd=win32gui.FindWindow('Qt5QWindowIcon','夜神模拟器')#是文件句柄，通过使用visual studio自带的spy++获得的。在工具栏中的 工具->spy++中,Qt5QWindowIcon是窗口类名，夜神模拟器 是窗口标题(窗口标题不一定是你窗口左上角显示的标题)
    #print(hwnd)
    #可操作窗口一般不是主窗口，一般是子窗口，子窗口必须使用FindWindowEx()函数来进行搜索
    hwnd = win32gui.FindWindowEx(hwnd, 0, 'Qt5QWindowIcon', 'ScreenBoardClassWindow');#在窗口句柄为hwnd的窗口中，（本例是 夜神模拟器），寻找子窗口，同样是在spy++工具中看到的窗口信息。Qt5QWindowIcon是窗口类名，ScreenBoardClassWindow是窗口标题
    #hwnd = win32gui.FindWindowEx(hwnd, 0, 'Qt5QWindowIcon', 'QWidgetClassWindow');#在窗口句柄为hwnd的窗口中，（本例是 ScreenBoardClassWindow），寻找子窗口，同样是在spy++工具中看到的窗口信息。Qt5QWindowIcon是窗口类名，ScreenBoardClassWindow是窗口标题
    return hwnd


