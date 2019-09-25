import interface.args as ARGS


from MyLibrary.Material.__Contain import __Contain
from numpy.random import binomial

class Proteome(__Contain):
    """
        
    """
    def __init__(self, proteins):
        super().__init__(proteins)


    def deal(self):
        """
            在这里根据蛋白名字对自身进行处理
            事实上, 每个 proteins 应至少包括以下特征: 总个数, 降解率, 作用产物, 单个效率, 作用对象, 
                其他难以描述的特征还包括: 与其他 proteins 或 genome 结合, 在胞内还是胞外发挥作用
            version 1.0.0: 
        """
        for protein in self._Contain__contains: # self():  # 加快速度
            try:
                degradeRate, reactant, efficiency, product, localization = protein.split(ARGS.CHARACTORSPLIT) # 首先能够将其转化为可以识别的类型
                degradeRate, efficiency = float(degradeRate), int(efficiency)

                # 模拟反应
                productSum = self.set(reactant, -efficiency*self[protein])
                self.set(product, productSum)

                # 模拟衰变
                degradeSum = binomial(self[protein], degradeRate)
                self.set(protein, -degradeSum)
            except Exception as e:
                #print(e)
                pass
