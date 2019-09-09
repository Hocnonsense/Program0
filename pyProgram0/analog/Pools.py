import interface.args as ARGS
from MyLibrary.Material.__Point import __Point

class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary


class Pools(object):
    """
        这个类只会有一个实例, 目的是作为土壤, 培养瓶, 池子, 96孔板, 地图之类, 每个位置上最多会有一个 Cell
    """
    def __init__(self):
        """
            初始化地图, 
            for 循环遍历并设置每个位点
        """
        self.pools = list(list())   #表示这是一个二维数组, 其实与一个 list() 一样
        
        pass

class Pool(object):
    def __init__(self, point, contain):
        self.__point = Point(point, "tuple")
        self.contain = contain

    def __getPoint(self):
        return self.__point()
    point = property(fget = __getPoint)

