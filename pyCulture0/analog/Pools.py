import interface.args as ARGS

from MyLibrary.Material.__Point import __Point
class Point(__Point):
    
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary


from analog.Proteome import Proteome as Contain

class Pool(Contain):
    def __init__(self, point, contains):
        super().__init__(contains)
        self.__point = Point(point, "tuple")
        self.occupy = None  # 指向该位置上的 Cell

    def __getPoint(self):
        return Point(self.__point(), "a new Point()")
    point = property(fget = __getPoint)


    def inDiffuse(self, tmp):
        """
            接受来自外界的物质
        """
        self.tmp.using += 1
        for contain in tmp:
            self.tmp.set(contain, tmp[contain])
        self.__doDiffusion(tmp)

    def outDiffuse(self):
        """
            将自身物质释放到外界
        """
        neighborsum, keepsum = ARGS.NEIGHBORRADIO
        self.tmp.using -= neighborsum
        contains = self()
        tmp = dict()
        for contain in contains:
            tmp[contain] = int(contains[contain]/(neighborsum+keepsum))
            self.tmp.set(contain, contains[contain] - tmp[contain]*neighborsum)
        self.__doDiffusion(tmp)
        return tmp

    def __doDiffusion(self, tmp):
        if self.tmp.using == 0 :
            self(self.tmp())
            self.tmp(mode = 'clear')
        pass



class Pools(object):
    """
        这个类只会有一个实例, 目的是作为一个可称之为土壤, 培养瓶, 池子, 96孔板, 地图的概念的实例, 每个位置上最多会有一个 Cell
    """
    def __init__(self, cells):
        """
            初始化地图, 
            for 循环遍历并设置每个位点
        """
        self.pools = list(list())   #表示这是一个二维数组, 其实与一个 list() 一样
        self.cells = cells
        try:
            self.__fileInit()
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

        self.__setBlankInit()

    def __setBlankInit(self):
        print("Warning: pools: 待条件合适, 应取消的特殊情况")
        for (x, y), contains in ARGS.SETINITPOOLS:
            self.pools[x][y](contains)

    

    def around(self, point, neighborlist = ARGS.NEIGHBORLIST):
        """
            list() Pools.around(Point() point)
            返回一个列表, 关于所有符合要求的 point 的坐标, 而非 pool
        """
        x, y = point
        neighbors = list()
        point = self.pools[x][y].point
        for dx, dy in neighborlist:
            x, y = point(dx, dy)
            neighbors.append((x, y))
        return neighbors

    def diffusion(self):
        pools = self.pools
        for poolx in pools:
            for pool in poolx:
                neighbors = self.around(pool.point())
                tmp = pool.outDiffuse()
                for x, y in neighbors:
                    self.pools[x][y].inDiffuse(tmp)


    def draw(self):
        """
            将 Pools 中的每个 Pool 转变为 (x, y), (r, g, b) 格式, 从而能够以图形形式实时显示
        """
        output, pools = list(), self.pools
        for poolx in pools:
            for pool in poolx:
                eachOne = pool.point(), (pool['r'], pool['g'], pool['b'])
                output.append(eachOne)
        return output
        