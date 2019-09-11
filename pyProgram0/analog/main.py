#2019-9-9 00:47:08
#version 1.0.0

from analog.Pools import Pools
from analog.Cells import Cells

pools, cells = None, None

def pyInit():
    global pools
    global cells
    pools = Pools()
    cells = Cells()

def pyStep():
    pools.diffusion()
    pass

def pyPassThrough():
    """
        输出将要画在 pygame 的画布上的图案
    """
    output = list()
    output = pools.draw() + cells.draw()
    return output

def pySave():
    pass

def pyEnd():
    pass