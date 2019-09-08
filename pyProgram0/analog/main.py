#2019-9-9 00:47:08
#version 1.0.0

def pyInit():
    print("maim.pyInit()")

def pyStep():
    print("main.pyStep()")

def pyPassThrough():
    cells = list()
    cells.append(((2, 4), (0, 50, 100)))
    return cells

def pyEnd():
    pass