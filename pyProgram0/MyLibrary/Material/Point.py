#2019-8-28 19:42:30
#version 1.0.0

class Point(object):
    """
    location of each point
    all Points move inside __XBoundary and __YBoundary
"""
    __XBoundary = 70
    __YBoundary = 30

    def __init__(self, x, y):
        self.__x , self.__y = self.__ifTuple(x, y)

    #X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    #Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)


    def __str__(self):
        return("{X:" + "{:.0f}".format(self.__x) + \
               ",Y:" + "{:.0f}".format(self.__y) + "}")

    def __call__(self, dx = 0, dy = 0):
        self.__x, self.__y = self.move(dx, dy)
        return((self.__x, self.__y))

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
        x = (self.__x + dx) % self.XBoundary()
        y = (self.__y + dy) % self.YBoundary()
        return(x, y)

    def around(self):
        neighbors = list()
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                x, y = self.move(dx, dy)
                neighbors.append((x, y))
        neighbors.remove((self.x, self.y))
        return neighbors
