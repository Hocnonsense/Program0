import interface.args as ARGS
from MyLibrary.Material.__Point import __Point

class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary


class Pools(object):
    """description of class"""
    def __init__(self):
        pass

class Pool(object):
    def __init__(self, point):
        self.point = Point(point, "tuple")
    pass

