class __Contain(object):
    """
        这个函数使其实例可进行字典操作
    """
    def __init__(self, contains):
        self.__contains = contains  # 这是一个数组, 储存环境中各种物质

    def __getitem__(self, contain):
        """
            该函数可使该类像字典一样使用
        """
        return self.__contains.get(contain, 0)

    def __setitem__(self, contain, sum):
        residue = self.__contains.get(contain, 0)   # 如果不含有该成分, 返回0
        if(sum + contained < 0):    # 需要的比原有的多
            sum = -residue
        self.__contains[contain] = sum + residue
        return -sum # 若sum>0, 返回负数代表释放到环境, 否则返回正数代表从环境中得到


