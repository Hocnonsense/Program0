from MyLibrary.Input.Mouse import Mouse
from MyLibrary.Input.Keyboard import key_input, toKeys, pressKeys
import time


def main():
    m = Mouse()
    m((50, 50)).click('l', 2)
    key_input("spacebar:_")
    pressKeys(['spacebar'])
    key_input("_")
    pressKeys(['enter'])
    m((10, 80)).click('l', 2)
    input()
    time.sleep(2)
    #输入网址打开网址 
    str1 = 'https://www.sina.com.cn'
    key_input(str1)
    pressKeys(['enter'])

    time.sleep(5)
    #按下Ctrl+s快捷键，打开文件保存对话框
    pressKeys(['ctrl', 's'])
    time.sleep(5)
    #键入文件名
    key_input("HAHA1.html")
    time.sleep(0.1)
    pressKeys(['enter'])
    #按下Ctrl+T快捷键，打开一个新的TAB页
    time.sleep(5)
    pressKeys(['ctrl', 't'])
    #输入网址并打开
    str1 = 'https://www.sohu.com'
    key_input(str1)
    pressKeys(['enter'])
