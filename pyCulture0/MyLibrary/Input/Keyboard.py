import win32api
import win32con
import time

from MyLibrary.Input.Keys import Str_Upders, VK_CODE, UPer_Lower_Code

#keyboard:
#   checker: 
#       IsUppercase()
#   actor:
#       oneKey(key)
#       twoKey(key)
#   grouper:
#       key_input(str)

def toKeys(str=""):
    """
    判断输入字符是键盘上位字符还是下位字符，如果是上位字符则需同时按下Shift键

"""
    toPress = list()
    if(Str_Upders.find(str)== -1):
        toPress.append(str)
    else:
        toPress.append('shift')    #因为是上位字符，需要同时按下Shift键
        toPress.append(UPer_Lower_Code[str])
    return(toPress)

def pressKeys(toPress):
    """
    keys is a list of keys, earlier_down is latter_up
    WARNING: ctrl, alt, win should be added first
"""
    for key in toPress:
        win32api.keybd_event(VK_CODE[key], 0, 0, 0)
    toPress.reverse()
    for key in toPress:
        win32api.keybd_event(VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
    pass

def key_input(str = '', split = ' '):
    """
    read each word in the string and 模拟按键
"""
    for c in str:
        print(toKeys(c))
        print(',')
        pressKeys(toKeys(c))

        time.sleep(0.01)
    


"""
keybd_event(BYTE bvk, BYTE bScan, DWORD dwFlags, DWORD dwExtraInfo):
    模拟键盘API函数，使用该函数可以相应的屏蔽键盘的动作. 触发一个按键事件，也就是说会产生一个 WM_KEYDOWN 或 WM_KEYUP 消息。

　　BYTE bVk :
        virtual-key code, 按键的虚拟键值，如回车键为vk_return, tab键为vk_tab（其他具体的参见附录：常用模拟键的键值对照表）

　　BYTE bScan :
        hardware scan code, 扫描码，一般不用设置，用0代替就行, 但在游戏中需要扫描码才能允许输入

　　DWORD dwFlags :
        flags specifying various function options, 选项标志，如果为keydown则置0即可，如果为keyup则设成"KEYEVENTF_KEYUP"

　　DWORD dwExtraInfo :
        additional data associated with keystroke, 一般也是置0即可
"""
