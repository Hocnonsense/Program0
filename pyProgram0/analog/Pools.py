import interface.args as ARGS

from MyLibrary.Material.__Point import __Point
class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary


class Pools(object):
    """
        这个类只会有一个实例, 目的是作为土壤, 培养瓶, 池子, 96孔板, 地图之类, 每个位置上最多会有一个 Cell
    """
    def __init__(self, filename = None):
        """
            初始化地图, 
            for 循环遍历并设置每个位点
        """
        self.pools = list(list())   #表示这是一个二维数组, 其实与一个 list() 一样
        try:
            self.__fileInit(filename)
        except Exception as e:
            self.__blankInit()
        
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


from MyLibrary.Material.__Contain import __Contain
class Pool(__Contain):
    def __init__(self, contains, point):
        __Contain.__init__(self, contains)
        self.__point = Point(point, "tuple")
        self.occupy = None  # 指向该位置上的 Cell
        self.__contains = contains  # 这是一个数组, 储存环境中各种物质

    def __getPoint(self):
        return self.__point()
    point = property(fget = __getPoint)
