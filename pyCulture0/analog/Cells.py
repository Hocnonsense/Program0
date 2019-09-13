import interface.args as ARGS

from analog.Pools import Point
from analog.Genome import Genome as Genome    # 只要是一个合理的基因组类型即可
from analog.Proteome import Proteome
import random

class Cell(object):
    def __init__(self, treeNumber, point, c):
        """
            这样的起始只能在显式调用 Cell() 时才能用到. 
        """
        self.genome = Genome(treeNumber)
        self.proteome = Proteome(c)
        self.point = Point(point, "tuple")

    def trend(self, neighbors):
        """
            假设环境中有一定的物质, 那么 cell 就会对其做出相应的反应. 
            从 proteome 中读取相应记录, 从 pools 中找到含该物质 未被占据且最多或最少 的一个, 随后移动到这个位置
        """
        prefer = self.proteome(ARGS.PREFERCONTAIN)
        aims = list()
        for point in neighbors:
            if(point.occupy == None):
                if aims == list():
                    aims.append(point)
                elif(point(prefer) == aims[0](prefer)):
                    aims = list(point)
                elif(pool(prefer) > aims[0](prefer)):
                    aims.append(point)
        if(aims == list()):
            aim = None
        else:
            aim = aims[random.randint(0, len(aim)-1)]
        return aim


class Cells(object):
    def __init__(self, pools):
        self.cells = list()
        self.pools = pools
        try:
            self.__fileInit(filename)
        except Exception as e:
            self.__blankInit()

    def __fileInit(self, filename = ""):
        """
            #   @Haor 记得填空
        """
        file = open(filename)
        for line in file:
            cell = line
            self.cells.append(cell)

    def __blankInit(self):
        """
            预设, 标准, 从头, 无记录的自动开始
        """
        for treeNumber, point, c in ARGS.SETINITCELLS:
            cell = Cell(treeNumber, point, c)
            self.cells.append(cell)


    def move(self):
        """
            cell 的运动行为
        """
        for cell in self.cells:
            neighbors = self.pools.around(cell.point())
            x, y = cell.point()
            points = list()
            points.append(self.pools.pools[x][y])
            prefer = cell.proteome[ARGS.PREFERCONTAIN]
            for x, y in neighbors:
                if(self.pools.pools[x][y].occupy == None):
                    if(self.pools.pools[x][y][prefer] == points[0][prefer]):
                        points.append(self.pools.pools[x][y])
                    elif(self.pools.pools[x][y][prefer] > points[0][prefer]):
                        points = list()
                        points.append(self.pools.pools[x][y])
            if(points == list()):
                point = cell.point()
            else:
                point = points[random.randint(0, len(points)-1)]
            (x0, y0), (x, y) = cell.point(), point.point()
            self.pools.pools[x0][y0].occupy = None
            cell.point.moveTo(x, y)
            self.pools.pools[x][y].occupy = None


    def draw(self):
        output = list()
        for cell in self.cells:
            eachOne = cell.point(), (cell.proteome()["r"], cell.proteome()["g"], cell.proteome()["b"])
            output.append(eachOne)
        return output

