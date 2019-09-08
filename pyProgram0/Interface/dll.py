#2019-9-8 23:47:40
#version 1.0.0

import interface.args as ARGS
from MyLibrary.Material.__Point import __Point
import analog.main as dll

class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary
    pass

def __show(eachOne):
    return eachOne

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
        node = __show(eachOne)
        nodes.append(node)

    return nodes

def pyEnd():
    dll.pyEnd()