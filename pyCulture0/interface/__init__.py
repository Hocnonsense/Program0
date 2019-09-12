"""
pyCulture0 are main files, all functions and args are from dll
dll is the MOST IMPORTANT file in this program. 

dll 抽象了所有具体的活动, 它可以方便地在调用 (python包 || 调用C++链接库) 之间来回切换, 公共函数仅在 pyCultue0 中被调用

#version 1.0.0 的 dll 调用 python 方法

args 包含所有可以独立变动的参数
这些参数最好只从 args 中被提取一次
如果需要调用 C++ 链接库, 则其中有一些参数必须要在 C++ 头文件中给出
"""
"""
pyCulture0 含有以下函数:
    refreash():
        刷新窗口, 同时判断是否退出
        有机会的话, 可以加入接受其他输入并响应的功能
        return running

    drawRect(screen, node, UnitSize):
        (x, y), color = node
        据此画出每个点
        如果有异常, 会进行提示

    display(XBoundary, YBoundary, UnitSize):
        创建窗口
        return screen

从运行开始就导入 savelog(), 将程序一切输出保存在文件中. 
import interface.dll as dll, dll 是最主要的程序包
导入其他模块
在 __main__ 主程序中:
    dll.起始
    display()
        dll.循环
        获取 dll.输出
            drawRect()
        refresh()
    dll.结束
    程序结束
"""
"""
interface.dll 包含以下函数:
    pyInit():
        起始
        
    pyStep():
        每步循环
    
    pyPassThrough():
        传递输出, 用于画图
    
    pyEnd():
        结束程序


    __show(eachOne):
        这是一个私有函数, 仅在 pyPassThrough() 中调用, 一开始只是为了将 c++链接库的输出处理为能被 python 接受的输出, 现在仅作为接口使用
"""