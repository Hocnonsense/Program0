"""
    version 1.0.0
    from C:\\Users\\Haor\\.conda\\envs\\Anaconda\\Lib\\site-packages\\PyHook3\\example.py
"""

import PyHook3
import pythoncom  # Magic utility that "redirects" to pythoncomxx.dll, only for getPyHookEvent()
import win32api

def sampleMouseEvent(event):
    print('MessageName:',event.MessageName)
    print('Message:',event.Message)
    print('Time:',event.Time)
    print('Window:',event.Window)
    print('WindowName:',event.WindowName)
    print('Position:',event.Position)
    print('Wheel:',event.Wheel)
    print('Injected:',event.Injected)
    print('---')
    
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

def sampleKeyboardEvent(event):
    #print('MessageName:',event.MessageName)
    #print('Message:',event.Message)
    #print('Time:',event.Time)
    #print('Window:',event.Window)
    #print('WindowName:',event.WindowName)
    print('Key:', event.Key)
    #print('KeyID:', event.KeyID)
    #print('ScanCode:', event.ScanCode)
    #print('Extended:', event.Extended)
    #print('Injected:', event.Injected)
    #print('Alt', event.Alt)
    #print('Transition', event.Transition)
    
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    if(event.Key == 'Escape'):
        stopPyHookEvent()
    return True

"""
除此之外，还有以下事件：
    鼠标事件：
        MouseAll
        MouseAllButtons
        MouseAllButtonsUp
        MouseAllButtonsDown
        MouseAllButtonsDbl
        MouseWheel
        MouseMove
        MouseLeftUp
        MouseLeftDown
        MouseLeftDbl
        MouseRightUp
        MouseRightDown
        MouseRightDbl
        MouseMiddleUp
        MouseMiddleDown
        MouseMiddleDbl
    键盘事件：
        KeyUp
        KeyDown
        KeyChar
        KeyAll
"""


global hm



def getPyHookEvent(mouseEvent = sampleMouseEvent, keyboardEvent = sampleKeyboardEvent):
    # create the hook mananger
    hm = PyHook3.HookManager()

    # register two callbacks
    #hm.MouseAllButtonsDown = mouseEvent
    #hm.MouseAllButtonsUp = mouseEvent
    #hm.KeyDown = keyboardEvent
    hm.KeyUp = keyboardEvent
    
    # hook into the mouse and keyboard events
    hm.HookMouse()
    hm.HookKeyboard()
    
    """
    对于命令行界面的编程，设置了钩子后还不够，因为脚本在成功挂钩后，就结束运行了。这个时候就需要使程序进入循环监听系统事件的状态。
比较简单的方法是使用Win32 Extensions package提供的PumpMessages()方法：
"""
    pythoncom.PumpMessages()

def stopPyHookEvent():
    """
    end the getting program. 
    PyHook3.HookManager() will __del__(self)
"""
    win32api.PostQuitMessage()

