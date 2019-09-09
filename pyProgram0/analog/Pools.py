import interface.args as ARGS

from MyLibrary.Material.__Point import __Point
class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary


from MyLibrary.Material.__Contain import __Contain
class Contain(__Contain):
    def __init__(self, contains):
        super().__init__(contains)
        self.using = 0

class Pool(__Contain):
    def __init__(self, point, contains):
        super().__init__(contains)
        self.__point = Point(point, "tuple")
        self.occupy = None  # 指向该位置上的 Cell
        self.tmp = Contain(dict()) # diffusion 中的暂存变量

    def __getPoint(self):
        return Point(self.__point(), "a new Point()")
    point = property(fget = __getPoint)


    def inDiffuse(self, tmp):
        self.tmp.using += 1
        for contain in tmp:
            self.tmp[contain] = tmp[contain]
        self.__doDiffusion(tmp)

    def outDiffuse(self):
        self.tmp.using += 2
        contains = self()
        tmp = dict()
        for contain in contains:
            tmp[contain] = int(contains[contain]/10)
            self.tmp[contain] = contains[contain] - tmp[contain]*8
        self.__doDiffusion(tmp)
        return tmp

    def __doDiffusion(self, tmp):
        if self.tmp.using == 10 :
            self._Contain__contains = self.tmp()
            self.tmp = Contain(dict())
        pass



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
        file = open(filename)
        self.pools = list(list())

    def __blankInit(self):
        """
            预设, 标准, 从头, 无记录的自动开始
        """
        for x in range(0, Point.XBoundary()):
            poolx = list()
            for y in range(0, Point.YBoundary()):
                contains = ARGS.CONTAINS
                pool = Pool((x, y), contains)
                poolx.append(pool)
            self.pools.append(poolx)

    

    def around(self, x, y):
        neighbors = list()
        point = self.pools[x][y].point
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                x, y = point(dx, dy)
                neighbors.append((x, y))
        neighbors.remove(point())
        return neighbors

    def diffusion(self):
        pools = self.pools
        for poolx in pools:
            for pool in poolx:
                x, y = pool.point()
                neighbors = self.around(x, y)
                tmp = pool.outDiffuse()
                for x, y in neighbors:
                    self.pools[x][y].inDiffuse(tmp)


    def drawPools(self):
        """
            将 Pools 中的每个 Pool 转变为 (x, y), (r, g, b) 格式
        """
        output, pools = list(), self.pools
        for poolx in pools:
            for pool in poolx:
                eachOne = pool.point(), (pool['r'], pool['g'], pool['b'])
                output.append(eachOne)
        return output
        