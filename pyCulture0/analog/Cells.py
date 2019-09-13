import interface.args as ARGS

from analog.Pools import Point
from analog.Genome import Vector as Genome    # 只要是一个合理的基因组类型即可
from analog.Proteome import Proteome
import random

class Cell(object):
    def __init__(self, treeNumber, point, genes, proteins):
        """
            这样的起始只能在显式调用 Cell() 时才能用到. 
        """
        self.genome = Genome(treeNumber, genes)
        self.proteome = Proteome(proteins)
        self.point = Point(point, "tuple")

    def transcript(self):
        """
            DNA -> 蛋白质 的过程. 定性而非定量
            以后可以添加降解的内容, 或者用多线程独立每个cell的行为. 
        """
        proteins = self.genome.commend()
        self.proteome(proteins)


class Cells(object):
    """
        多个 pool 与 Cell 之间的关系, 只能由 Cells 处理. 
        细胞的移动问题, 需要在这个层次中解决
    """
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
        for treeNumber, point, genes, proteins in ARGS.SETINITCELLS:
            cell = Cell(treeNumber, point, genes, proteins)
            self.cells.append(cell)


    def move(self):
        """
            cell 的运动行为
            # version 1.0.0 追随某些物质的行为
            假设环境中有一定的物质, 那么 cell 就会对其做出相应的反应. 
            从 proteome 中读取相应记录, 从 pools 中找到含该物质 未被占据且最多或最少 的一个, 随后移动到这个位置
        """
        for cell in self.cells:
            cell.transcript()

            neighbors = self.pools.around(cell.point()) # 周围可以去的地方
            x, y = cell.point() # 此时的位置
            points = list() # 收录选择去的点
            points.append(self.pools.pools[x][y])
            prefer = cell.proteome[ARGS.PREFERCONTAIN]  # 选择可以去的点的依据

            for x, y in neighbors:
                if(self.pools.pools[x][y].occupy == None):
                    if(self.pools.pools[x][y][prefer] == points[0][prefer]):
                        points.append(self.pools.pools[x][y])
                    elif(self.pools.pools[x][y][prefer] < points[0][prefer]):
                        points = list()
                        points.append(self.pools.pools[x][y])
            point = points[random.randint(0, len(points)-1)]
            self.__move(cell, point.point())

    def __move(self, cell, point):
        (x0, y0), (x, y) = cell.point(), point
        self.pools.pools[x0][y0].occupy = None
        cell.point.moveTo(x, y)
        self.pools.pools[x][y].occupy = cell


    def draw(self):
        output = list()
        for cell in self.cells:
            eachOne = cell.point(), (cell.proteome()["r"], cell.proteome()["g"], cell.proteome()["b"])
            output.append(eachOne)
        return output

