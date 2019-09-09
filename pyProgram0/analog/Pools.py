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
        
    def __fileInit(self, filename = ""):
        """
            #   @Haor 记得填空
        """
        self.pools = list(list())

    def __blankInit(self):
        """
            标准, 从头开始, 无记录的自动开始
        """
        for x in range(0, Point().XBoundary()):
            poolx = list()
            for y in range(0, Point().YBoundary()):
                contains = ARGS.CONTAINS
                pool = Pool((x, y), contains)
                poolx.append(pool)
            self.pools.append(poolx)



class Pool(object):
    def __init__(self, point, contains):
        self.__point = Point(point, "tuple")
        self.occupy = None  # 指向该位置上的 Cell
        self.contains = contains  # 这是一个数组, 储存环境中各种物质

    def __getPoint(self):
        return self.__point()
    point = property(fget = __getPoint)

    def __getitem__(self, contain):
        """
            该函数可使该类像字典一样使用
        """
        return self.contains.get(contain, 0)

    def __setitem__(self, contain, sum):
        residue = self.contains.get(contain, 0)   # 如果不含有该成分, 返回0
        if(sum + contained < 0):    # 需要
            sum, residue = residue, 0


