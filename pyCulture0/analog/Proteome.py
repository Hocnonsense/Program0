import interface.args as ARGS


from MyLibrary.Material.__Contain import __Contain as Contain
from numpy.random import binomial

class Proteome(Contain):
    """
        
    """
    def __init__(self, proteins):
        super().__init__(proteins)
        self.tmp = Contain(dict()) # diffusion 中的暂存变量
        self.tmp.using = 0


    def deal(self):
        """
            在这里根据蛋白名字对自身进行处理
            需要将其重构, 至少要分离出几个函数: 识别蛋白, 找出反应物, 
            事实上, 每个 proteins 应至少包括以下特征: 降解率, 作用产物, 单个效率, 作用对象, 
            version 1.0.0: 
        """
        for protein in self._Contain__contains: # self():  # 加快速度
            try:
                degradeRate, reactant, efficiency, product, localization = protein.split(ARGS.CHARACTORSPLIT) # 首先能够将其转化为可以识别的类型
                degradeRate, efficiency = float(degradeRate), int(efficiency)

                # 判断 _酶的定位, 发生反应的位置_
                if localization == ARGS.INTRALOCATION:
                    # 模拟反应
                    productSum = self.set(reactant, -efficiency*self[protein])
                    self.set(product, productSum)
                    # 模拟衰变
                    degradeSum = binomial(self[protein], degradeRate)
                    self.set(protein, -degradeSum)
                elif localization == ARGS.EXTRALOCATION:
                    productSum = self.set(protein, -self[protein])  # send itself to tmp
                    self.tmp.set(protein, productSum)
                elif localization == ARGS.TRANSLOCATION:
                    productSum = self.set(protein, -self[protein])
                    #print(prproductSum)
                    self.tmp.set(protein, productSum)
            except Exception as e:
                #print(e)
                assert len(protein.split(ARGS.CHARACTORSPLIT)) == 1 # 不是蛋白
        #print(self.tmp())