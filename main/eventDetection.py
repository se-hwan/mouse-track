import win32api
from win32 import win32gui
import msvcrt
import numpy as np

def eventDetection(x,y,clicks,run_flag,state_left,state_right):
    if msvcrt.kbhit():
        if msvcrt.getwche() == '\r':
            run_flag = False
    left = win32api.GetKeyState(0x01)
    right = win32api.GetKeyState(0x02)
    currentX, currentY = win32gui.GetCursorPos()
    #print(currentX,currentY)
    x=np.append(x,currentX)
    y=np.append(y,currentY)
    if left != state_left:  # Button state changed
        state_left = left
        if left < 0:
            #print('Left Button Pressed')
            clicks = np.append(clicks,1)
    elif right != state_right:
        state_right = right
        if right < 0:
            #print('Right Button Pressed')
            clicks = np.append(clicks,2)
    else:
        clicks = np.append(clicks,0)
    return x,y,clicks,run_flag
