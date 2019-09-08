#2019-9-8 23:47:40
#version 1.0.0

import interface.args as ARGS
from MyLibrary.Material.__Point import __Point

class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary
    pass

def pyInit():
    args = (Point.XBoundary(), Point.YBoundary()), ARGS.UnitSize
    return args

def pyStep():
    pass

def pyPassThrough():
    Nodes = list()
    exampleNode = (5, 5), (0, 127, 255) #   @Haor: delete if proper
    Nodes.append(exampleNode)
    return Nodes