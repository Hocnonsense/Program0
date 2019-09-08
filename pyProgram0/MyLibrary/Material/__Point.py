#2019-8-28 19:42:30
#version 1.0.0

class __Point(object):
    """
    location of each point
    all Points move inside __XBoundary and __YBoundary
"""
    __XBoundary
    __YBoundary

    def __init__(self, x, y):
        self.__x , self.__y = self.__ifTuple(x, y)

    #X property
    def __getx(self): return self.__x
    def __setx(self, x): self.__x = x
    x = property(__getx, __setx)

    #Y property
    def __gety(self): return self.__y
    def __sety(self, y): self.__y = y
    y = property(__gety, __sety)


    def __str__(self):
        return("{X:" + "{:.0f}".format(self.__x) + \
               ",Y:" + "{:.0f}".format(self.__y) + "}")

    def __call__(self, dx = 0, dy = 0):
        """
            return (x+dx, y+dy)
        """
        x = (self.__x + dx) % self.XBoundary()
        y = (self.__y + dy) % self.YBoundary()
        return(x, y)

    def __ifTuple(self, tuple_, y_):
        """
            to suit the situation if return a tuple
        """
        try:
            x, y = tuple_
        except Exception as e:
            x, y = tuple_, y_
        return(x, y)

    @classmethod
    def XBoundary(cls):
        return cls.__XBoundary
    @classmethod
    def YBoundary(cls):
        return cls.__YBoundary

    def move(self, dx, dy):
        self.__x, self.__y = self.__call__(dx, dy)
        return(self.__x, self.__y)

    def moveTo(self, x, y):
        """
            not recommond
        """
        self.__x, self.__y = x, y
        return(self.__x, self.__y)

    def around(self):
        neighbors = list()
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                x, y = self.__call__(dx, dy)
                neighbors.append((x, y))
        neighbors.remove((self.x, self.y))
        return neighbors
