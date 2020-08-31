import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection

def plot(x,y,clicks):
    nPoints = len(x)
    nClickPoints = len(clicks)
    diff = nPoints-nClickPoints
    print("Data points: ", nPoints)
    #plot clicks here, diff marker for L and R clicks
    for i in range(nClickPoints):
        if (clicks[i]==1):
            plt.plot(x[i]+20,y[i]+20,marker ='x',alpha = 0.5,color='green',
                     markersize = 8)
        elif (clicks[i]==2):
            plt.plot(x[i]+20,y[i]+20,marker ='+',alpha=0.5,color='blue',
                     markersize = 8)


    # plot visuals

    colorGrad = np.linspace(0,10,nPoints)
    points = np.array([x+20,y+20]).T.reshape(-1,1,2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=plt.get_cmap('Reds'),norm=plt.Normalize(0, 10))
    lc.set_array(colorGrad)
    lc.set_linewidth(1.5)
    plt.gca().add_collection(lc)

    plt.xlim(0,1576) # real size is 864x1536
    plt.ylim(904,0) 
    plt.axis('off')
    plt.gca().add_patch(Rectangle((10, 10),1556, 884, fc='None',lw=1,ec='k'))
    plt.plot(axisbg='k')
    figName = "figure.png" # change saved image name as desired
    
    plt.savefig(figName, dpi = 300)
    plt.show()

