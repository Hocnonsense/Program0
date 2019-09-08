#2019-9-8 23:47:40
#version 1.0.0

import interface.args as ARGS
from MyLibrary.Material.__Point import __Point
import analog.main as dll

class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary
    pass


def pyInit():
    args = (Point.XBoundary(), Point.YBoundary()), ARGS.UnitSize
    dll.pyInit()
    return args

def pyStep():
    dll.pyStep()
    pass

def pyPassThrough():
    nodes = list()

    output = dll.pyPassThrough()
    for eachOne in output:
        node = eachOne
        nodes.append(node)

    return nodes

def pyEnd():
    dll.pyEnd()