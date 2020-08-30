from win32 import win32gui
import win32api, win32con
import msvcrt, time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection


# split into start script
print("Width =", win32api.GetSystemMetrics(0))
print("Height =", win32api.GetSystemMetrics(1))
x = np.array([])
y = np.array([])
clicks = np.array([])

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Left button down = 0 or 1. Button up = -127 or -128
while True:

# split clicking and mouse posn tracking into separate files
    if msvcrt.kbhit():
        if msvcrt.getwche() == '\r':
            break
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
    time.sleep(0.005)
# need to add 2 more vectors 


# split into plot files
# need to make pretty

# plotting
nPoints = len(x)
nClickPoints = len(clicks)
diff = nPoints-nClickPoints
print(nPoints)
print(nClickPoints)
#plot clicks here, diff marker for L and R clicks
for i in range(nClickPoints):
    if (clicks[i]==1):
        plt.plot(x[i]+20,y[i]+20,marker ='x',alpha = 0.5,color='green',
                 markersize = 8)
    elif (clicks[i]==2):
        plt.plot(x[i]+20,y[i]+20,marker ='+',alpha=0.5,color='blue',
                 markersize = 8)
        
colorGrad = np.linspace(0,10,nPoints)
points = np.array([x+20,y+20]).T.reshape(-1,1,2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, cmap=plt.get_cmap('Blues'),norm=plt.Normalize(0, 10))
lc.set_array(colorGrad)
lc.set_linewidth(1)
plt.gca().add_collection(lc)


# plot visuals
plt.xlim(0,1576) # real size is 864x1536
plt.ylim(904,0) 
plt.axis('off')
plt.gca().add_patch(Rectangle((10, 10),1556, 884, fc='None',lw=1,ec='k'))
plt.savefig('test.png', dpi = 500)
plt.show()




