import interface.args as ARGS

from analog.Pools import Point
from analog.Genome import Vector as Genome    # 只要是一个合理的基因组类型即可
from analog.Proteome import Proteome
import random


"""
现在, 我希望能加入这样的功能:
    cell 可以按照 proteins 的要求与外界交换物质
        在每次循环中, 对 proteins 进行遍历, 根据 proteins 做出相对应的操作
        第一步是提供一个能模拟 proteins 功能的函数, 并给出对应的 proteins 
        第二步是添加 proteins 对细胞功能的影响, 比如与外界交换物质
            目前 proteins 可以在 cell 内完成反应
            但是 如何在 pool 和 cell 间交换物质, 尚待解决
    cell 可以根据外界的物质相对浓度运动
"""

class Cell(object):
    def __init__(self, treeNumber: int, point: Point, genes: str, proteins: dict):  
        """
            这样的起始只能在显式调用 Cell() 时才能用到, 也就是 Cells.init() 中才可以用. 
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
        for protein in proteins:
            self.proteome.set(protein, 1)

    def reaction(self):
        self.proteome.deal()

    def Diffuse(self, pool):
        """
            cell 内与 pool 的交流
            发挥作用的物质保存在 proteome.tmp 中. 
            要求 localization == ARGS.TRANSLOCATION
        """
        from numpy.random import binomial
        tmp = self.proteome.tmp
        for protein in tmp():
            
            try:
                degradeRate, reactant, efficiency, product, localization = protein.split(ARGS.CHARACTORSPLIT) # 首先能够将其转化为可以识别的类型
                degradeRate, efficiency = float(degradeRate), int(efficiency)
                #print(protein)
                # 判断 _酶的定位, 发生反应的位置_
                if localization == ARGS.TRANSLOCATION:
                    limit = min(self.proteome[reactant], pool[product]) # 找出最少的值并保存
                    tmp({"limit":limit})
                    # 模拟转运
                    productSum = tmp.set("limit", -efficiency*tmp[protein])
                    self.proteome.set(reactant, -productSum)
                    self.proteome.set(product, productSum)
                    pool.set(product, -productSum)
                    pool.set(reactant, productSum)
                    # 模拟衰变
                    degradeSum = binomial(tmp[protein], degradeRate)
                    tmp.set(protein, -degradeSum)
                elif localization == ARGS.INTRALOCATION:
                    # 一般不会出现
                    assert False
                    pass
                elif localization == ARGS.EXTRALOCATION:
                    protein = protein.replace(ARGS.EXTRALOCATION, ARGS.INTRALOCATION)   # 意味着将其转运到膜外并去除标签, 将在另一个世界发挥作用
                    productSum = tmp.set(protein, -tmp[protein])    # send itself out
                    pool.set(protein, productSum)    # send itself out
            except Exception as e:
                #print(e)
                assert len(protein.split(ARGS.CHARACTORSPLIT)) == 1 # 不是蛋白


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
            从 proteome 中读取相应记录, 从 pools 中找到 _含该物质未被占据且最多或最少_ 的一个, 随后移动到这个位置
            # version 1.0.1 
            不应该决定性地去往某个区域, 最好能按照概率, 倾向于往比较好的地方移动
        """
        for cell in self.cells:
            cell.transcript()

            neighbors = self.pools.around(cell.point()) # 周围可以去的地方
            x, y = cell.point() # 此时的位置
            points = list() # 收录选择去的点
            points.append(self.pools.pools[x][y])
            prefer = 'r'    # cell.proteome[ARGS.PREFERCONTAIN]  # 选择可以去的点的依据

            for x, y in neighbors:
                if(self.pools.pools[x][y].occupy == None):
                    #print(self.pools.pools[x][y][prefer], end = ", ")
                    if(self.pools.pools[x][y][prefer] == points[0][prefer]):
                        points.append(self.pools.pools[x][y])
                    elif(self.pools.pools[x][y][prefer] > points[0][prefer]):
                        points = list()
                        points.append(self.pools.pools[x][y])
            point = points[random.randint(0, len(points)-1)]
            self.__move(cell, point.point())

            cell.reaction()
            x, y = cell.point()
            cell.Diffuse(self.pools.pools[x][y])

    def __move(self, cell, point):
        (x0, y0), (x, y) = cell.point(), point
        self.pools.pools[x0][y0].occupy = None
        cell.point.moveTo(x, y)
        self.pools.pools[x][y].occupy = cell


    def draw(self):
        """
            将 Cells 中的每个 Cell 转变为 (x, y), (r, g, b) 格式, 从而能够以图形形式实时显示
        """
        output = list()
        for cell in self.cells:
            eachOne = cell.point(), (cell.proteome()["r"], cell.proteome()["g"], cell.proteome()["b"])
            output.append(eachOne)
            #print(cell.proteome())
        return output

