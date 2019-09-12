import interface.args as ARGS

from analog.Pools import Point
from analog.Genome import Genome as Genome    # 只要是一个合理的基因组类型即可
from analog.Proteome import Proteome

class Cell(object):
    def __init__(self, treeNumber, point, c):
        self.genome = Genome(treeNumber)
        self.proteome = Proteome(c)
        self.point = Point(point, "tuple")


class Cells(object):
    def __init__(self):
        self.cells = list()
        try:
            self.__fileInit(filename)
        except Exception as e:
            self.__blankInit()

    def __fileInit(self, filename = ""):
        """
            #   @Haor 记得填空
        """
        file = open(filename)
        self.cells = list()

    def __blankInit(self):
        """
            预设, 标准, 从头, 无记录的自动开始
        """
        for treeNumber, point, c in ARGS.SETINITCELLS:
            cell = Cell(treeNumber, point, c)
            self.cells.append(cell)


    def draw(self):
        output = list()
        for cell in self.cells:
            eachOne = cell.point(), (cell.proteome()["r"], cell.proteome()["g"], cell.proteome()["b"])
            output.append(eachOne)
        return output