#2019-9-8 23:47:40
#version 1.0.0

import interface.args as ARGS
import analog.main as dll


def __show(eachOne):
    return eachOne

def pyInit():
    args = (ARGS.XBoundary, ARGS.YBoundary), ARGS.UnitSize
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
    print("save successfully")