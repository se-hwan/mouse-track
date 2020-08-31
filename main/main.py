import time
import numpy as np
from initialize import initialize
from plot import plot
from eventDetection import eventDetection

# initialization
x,y,clicks,state_left,state_right,run_flag = initialize()

# main loop
while run_flag:
    x,y,clicks,run_flag = eventDetection(x,y,clicks,run_flag,state_left,state_right)
    time.sleep(0.001) # modify as needed, or comment out

# plotting
plot(x,y,clicks)

# function to save values to txt
saveName = "data.txt" # modify this to be more descriptive as needed
saveFile = open(saveName,"w")
posnData = np.column_stack((x,y))
np.savetxt(saveFile,posnData)
saveFile.close()

