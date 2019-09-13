class __Contain(object):
    """
        这个函数使其实例可进行字典操作
    """
    def __init__(self, contains):
        self.__contains = dict(contains)  # 这是一个字典, 储存环境中各种物质

    def __getitem__(self, contain):
        """
            该函数可使该类像字典一样使用
        """
        return self.__contains.get(contain, 0)

    def __setitem__(self, contain, sum):
        residue = self.__contains.get(contain, 0)   # 如果不含有该成分, 返回0
        if(sum + residue < 0):    # 需要的比原有的多
            sum = -residue
        self.__contains[contain] = sum + residue
        return -sum # 若sum>0, 返回负数代表释放到环境, 否则返回正数代表从环境中得到
    
    def __call__(self, contains = None):
        """
            没有输入则拷贝 self.字典 并返回
            输入一个字典则更新 self.字典, 这个方法并不会把未提到的成分删除
        """
        if contains == None:
            return dict(self.__contains)
        for contain in contains:
            self.__contains[contain] = contains[contain]
