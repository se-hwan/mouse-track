import win32api
import numpy as np



def initialize():
    print("Width =", win32api.GetSystemMetrics(0))
    print("Height =", win32api.GetSystemMetrics(1))
    run_flag=True
    x = np.array([])
    y = np.array([])
    clicks = np.array([])
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Left button down = 0 or 1. Button up = -127 or -128
    return x,y,clicks,state_left,state_right,run_flag
