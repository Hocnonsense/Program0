"""
for analog.Pools.Point()
to set the boundary
    __XBoundary = ARGS.XBoundary
    __YBoundary = ARGS.YBoundary
    args = (ARGS.XBoundary, ARGS.YBoundary), ARGS.UnitSize
"""
XBoundary = 70
YBoundary = 30

"""
设定起始时每个 Pool 中含有的各种物质, 成分, 信息素
                contains = ARGS.CONTAINS
"""
CONTAINS = {
    'r' : 0, 
    'g' : 0, 
    'b' : 0, 
}

"""
定义每个 pool 邻居, 可到达, 可扩散至的相对位置
定义分配时自留和流出的比例, 假定流出的每份为 1
    def around(self, x, y, neighborlist = ARGS.NEIGHBORLIST):
        neighborsum, keepsum = ARGS.NEIGHBORRADIO
"""
NEIGHBORLIST = [
    #(-1,-1), (-1, 0), (-1, 1), ( 0,-1), ( 0, 1), ( 1,-1), ( 1, 0), ( 1, 1), #   九宫格模式
    (-1, 0), ( 0,-1), ( 0, 1), ( 1, 0), #   上下左右模式
]
NEIGHBORRADIO = (
    len(NEIGHBORLIST), 
    2
)

"""
for pyInit()
to set the Size
    args = (ARGS.XBoundary, ARGS.YBoundary), ARGS.UnitSize
"""
UnitSize = 10