import win32api
import win32con
from ctypes import Structure, c_ulong, windll
import time

# Mouse:
#   location: 
#       class POINT 
#       __call__()


class Mouse(object):
    """
    for all mouseActions:
        get mouseSituation:
            Mouse()()
        set mouseSituation at (x, y):
            Mouse()(x, y)
        click [LEFT / RIGHT / MIDDLE] for n times:
            Mouse().click(['l' / 'r' / 'm'], n)
        roll the wheel:
            Mouse().wheel()
        press mouse and pull it:
            Mouse().pull()


    not recommend:
        click multipy at same time:
            Mouse().click2([key1, key2, ...])
"""
    def __init(self):
        self.__POINT = POINT()

    def __call__(self, POINT = (None, None)):
        """
        if input point like (x, y):
            move Mouse to (x, y) and wait for 0.05s
        if FAULT *args:
            return site
"""
        try:
            x, y = POINT
            windll.user32.SetCursorPos(x, y)
            time.sleep(0.05)
            return(self)
        except Exception as e:
            windll.user32.GetCursorPos(byref(self.__POINT))
            return(self.__POINT.x, self.__POINT.y)

    def click(self, MOUSEEVENT = 'l', TIMES = 1):
        """
        MOUSEEVENTF[0] MUST in ['l', 'r', 'm', ] for ['LEFT', 'RIGHT', 'MIDDLE']
        click for TIMES times
"""
        EVENTF = MOUSEEVENT[0].upper()
        if EVENTF not in ["L", "R", "M"]:
            print("click ERROR: illigal mouseClickAction!")
            input()
        for i in range(0, TIMES):
            dn, up = EVENTF + 'DN', EVENTF + 'UP'
            win32api.mouse_event((Click_Code[dn]), 0, 0, 0, 0) # click at mouse's situation
            win32api.mouse_event((Click_Code[up]), 0, 0, 0, 0) # click at mouse's situation

    def click2(self, MOUSEEVENTS = ['l', ]):
        """
        useless but might be helpful
        MOUSEEVENTF should be list(event)
        each event[0] in ['l', 'r', 'm', ] for ['LEFT', 'RIGHT', 'MIDDLE']

        按多个键, 按顺序先按后松
"""
        _mouseUpEvents = list()
        for event in MOUSEEVENTS:
            EVENTF = event[0].upper()
            dn, up = EVENT + 'DN', EVENT + 'UP'
            win32api.mouse_event((Click_Code[dn]), 0, 0, 0, 0) # click at mouse's situation
            _mouseUpEvents = [up] + _mouseUpEvents
        for up in _mouseUpEvents:
            win32api.mouse_event((Click_Code[up]), 0, 0, 0, 0) # click at mouse's situation

    def wheel(self):
        """
        action for rolling the wheel
"""
        phass = "sorry, UNfinished"
        print(phass)
        return(phass)

    def pull(self, MOUSEEVENT, POINTS):
        """
        MOUSEEVENTF[0] MUST in ['l', 'r', 'm', ] for ['LEFT', 'RIGHT', 'MIDDLE']
        POINTS is a list of point(x, y) that the mouse pass by. 
"""
        phass = "sorry, UNfinished"
        print(phass)
        return(phass)

    class POINT(Structure):
        """
        ONLY for get_mouse_point()
        Strutrue() is an abstruct class
    """
        _fields_ = [("x", c_ulong), ("y", c_ulong)]


Click_Code = {
"LDN" : win32con.MOUSEEVENTF_LEFTDOWN   ,
"LUP" : win32con.MOUSEEVENTF_LEFTUP     ,
"RUP" : win32con.MOUSEEVENTF_RIGHTDOWN  ,
"RDN" : win32con.MOUSEEVENTF_RIGHTUP    ,
"MUP" : win32con.MOUSEEVENTF_MIDDLEDOWN ,
"MDN" : win32con.MOUSEEVENTF_MIDDLEUP   ,

} 

dwFlags = [
win32con.MOUSEEVENTF_ABSOLUTE   ,
win32con.MOUSEEVENTF_MOVE       ,
win32con.MOUSEEVENTF_LEFTDOWN   ,
win32con.MOUSEEVENTF_LEFTUP     ,
win32con.MOUSEEVENTF_RIGHTDOWN  ,
win32con.MOUSEEVENTF_RIGHTUP    ,
win32con.MOUSEEVENTF_MIDDLEDOWN ,
win32con.MOUSEEVENTF_MIDDLEUP   ,
win32con.MOUSEEVENTF_WHEEL      ,
]

"""
mouse_event (long dwFlags,long dx,long dy,long cButtons,long dwExtraInfo):
    Windows API 中 mouse_event 函数
    
    long dwFlags :
        MOUSEEVENTF_ABSOLUTE：表明参数 dX，dy 含有规范化的绝对坐标。[[2]{a:b}]
        MOUSEEVENTF_MOVE：表明发生移动。
        MOUSEEVENTF_LEFTDOWN：表明接按下鼠标左键。
        MOUSEEVENTF_LEFTUP：表明松开鼠标左键。
        MOUSEEVENTF_RIGHTDOWN：表明按下鼠标右键。
        MOUSEEVENTF_RIGHTUP：表明松开鼠标右键。
        MOUSEEVENTF_MIDDLEDOWN：表明按下鼠标中键。
        MOUSEEVENTF_MIDDLEUP：表明松开鼠标中键。
        MOUSEEVENTF_WHEEL：在Windows NT中如果鼠标有一个轮，表明鼠标轮被移动。移动的数量由dwData给出。[[1]{a:b}]
    
    long dx, long dy :
        指定鼠标沿x轴的绝对位置或者从上次鼠标事件产生以来移动的数量，依赖于 MOUSEEVENTF_ABSOLUTE 的设置. [[2]{b:a}]
    
    long cButtons : 
        dwFlags 为 MOUSEEVENTF_WHEEL，则 dwData 指定鼠标轮移动的数量。如果 dwFlagsS 不是 MOUSEEVENTF_WHEEL，则 dWData 应为零。[[1]{b:a}]
    
    long dwExtraInfo ：
        指定与鼠标事件相关的附加32位值。应用程序调用函数 GetMessageExtraInfo 来获得此附加信息。
"""
