import matplotlib.pyplot as plot
import numpy as np
from typing import Tuple
from typing import List

"""
    Programme to draw triangle of triangles in matplotlib
"""

# width of the plot
period = 10
#Need double the steps
steps = period * 2


def GetArrayValuesPositive(startX: int) -> Tuple[List[int],List[int]]:
    """
        Calculates the lines in the positive gradient
        Returns lists of X and Y coordinates
    """
    endX = int(startX/2 + period)
    xVals = []
    yVals = []
    for i in range(startX, endX):
        xVals.append(i)
        yVals.append(i - startX)

    return xVals, yVals

def GetArrayValuesNegative(startX: int) -> Tuple[List[int],List[int]]:
    """
        Calculates the lines in the negative gradient
        Returns lists of X and Y coordinates
    """

    start = int(startX / 2)
    xVals = []
    yVals = []

    for i in range(start, startX + 1):
        xVals.append(i)
        yVals.append(startX - i)
    return xVals, yVals

def GetArrayValuesHorizontal(startX: int) -> Tuple[List[int],List[int]]:
    """
        Calculates the horizontal lines
        Returns lists of X and Y coordinates
    """
    start = int(startX/2)
    xVals = []
    yVals = []
    for i in range(start, steps - start - 1):
        xVals.append(i)
        yVals.append(start)

    return xVals, yVals

# calculate the coordinates for each part of the plot
for i in range(0,steps,2):
    x,y = GetArrayValuesPositive(i)
    nx,ny = GetArrayValuesNegative(i)
    hx,hy = GetArrayValuesHorizontal(i)
    plot.plot(x,y, 'r-')
    plot.plot(nx,ny, 'r-')
    plot.plot(hx,hy, 'r-')

plot.xlim([0, steps])
plot.xticks(np.arange(0, steps, 1))
plot.yticks(np.arange(0, period + 1, 1))
plot.title("Triangles")
plot.show()