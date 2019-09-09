"""
pyProgame0 are main files, all functions and args are from dll
dll is the MOST IMPORTANT file in this program. 

dll 抽象了所有具体的活动, 它可以方便地在调用 (python包 || 调用C++链接库) 之间来回切换

#version 1.0.0 的 dll 调用 python 方法

args 包含所有可以独立变动的参数
这些参数最好只从 args 中被提取一次
如果需要调用 C++ 链接库, 则其中有一些参数必须要在 C++ 头文件中给出
"""
