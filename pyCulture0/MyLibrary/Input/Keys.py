Str_Upders='!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

Uper_Code=[
'~',    '!',    '@',    '#',    '$',    '%',    '^',    '&',    '*',    '(',    ')',    '_',    '+',    
'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P',    '{',    '}',    '|',
'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L',            ':',    '"',    
'Z',    'X',    'C',    'V',    'B',    'N',    'M',                            '<',    '>',    '?'
]

UPer_Lower_Code = {
'~':'`','!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9',')':'0','_':'-','+':'=',
'Q':'q','W':'w','E':'e','R':'r','T':'t','Y':'y','U':'u','I':'i','O':'o','P':'p','{':'[','}':']','|':'\\',
'A':'a','S':'s','D':'d','F':'f','G':'g','H':'h','J':'j','K':'k','L':'l',        ':':';','"':"'",
'Z':'z','X':'x','C':'c','V':'v','B':'b','N':'n','M':'m',                        '<':',','>':'.','?':'/',
}


VK_BASIC_CODE = {
'backspace':0x08,   'tab':0x09,         'clear':0x0C,       'enter':0x0D,       'shift':0x10,       'ctrl':0x11,        'alt':0x12,
'pause':0x13,       'caps_lock':0x14,   'esc':0x1B,         'spacebar':0x20,    
'page_up':0x21,     'page_down':0x22,   'end':0x23,         'home':0x24,
'left_arrow':0x25,  'up_arrow':0x26,    'right_arrow':0x27, 'down_arrow':0x28,
'select':0x29,      'print':0x2A,       'execute':0x2B,
'print_screen':0x2C,'ins':0x2D,         'del':0x2E,         
'help':0x2F,
'0':0x30,   '1':0x31,   '2':0x32,   '3':0x33,   '4':0x34,   '5':0x35,   '6':0x36,   '7':0x37,   '8':0x38,   '9':0x39,   
'a':0x41,   'b':0x42,   'c':0x43,   'd':0x44,   'e':0x45,   'f':0x46,   'g':0x47,   'h':0x48,   'i':0x49,   'j':0x4A,   
'k':0x4B,   'l':0x4C,   'm':0x4D,   'n':0x4E,   'o':0x4F,   'p':0x50,   'q':0x51,   'r':0x52,   's':0x53,   't':0x54,   
'u':0x55,   'v':0x56,   'w':0x57,   'x':0x58,   'y':0x59,   'z':0x5A,   
'numpad_0':0x60,    'numpad_1':0x61,    'numpad_2':0x62,    'numpad_3':0x63,    'numpad_4':0x64,    
'numpad_5':0x65,    'numpad_6':0x66,    'numpad_7':0x67,    'numpad_8':0x68,    'numpad_9':0x69,    
'multiply_key':0x6A,    
'add_key':0x6B,
'separator_key':0x6C,
'subtract_key':0x6D,
'decimal_key':0x6E,
'divide_key':0x6F,
'F1':0x70,  'F2':0x71,  'F3':0x72,  'F4':0x73,  'F5':0x74,  'F6':0x75,  'F7':0x76,  'F8':0x77,  'F9':0x78,  'F10':0x79,
'F11':0x7A, 'F12':0x7B, 'F13':0x7C, 'F14':0x7D, 'F15':0x7E, 'F16':0x7F, 'F17':0x80, 'F18':0x81, 'F19':0x82, 'F20':0x83,
'F21':0x84, 'F22':0x85, 'F23':0x86, 'F24':0x87, 
'num_lock':0x90,    'scroll_lock':0x91,
'left_shift':0xA0,  'right_shift ':0xA1,'left_control':0xA2,'right_control':0xA3,
'left_menu':0xA4,   'right_menu':0xA5,
'browser_back':0xA6,    'browser_forward':0xA7, 'browser_refresh':0xA8, 
'browser_stop':0xA9,    'browser_search':0xAA,  'browser_favorites':0xAB,   'browser_start_and_home':0xAC,
'volume_mute':0xAD, 'volume_Down':0xAE, 'volume_up':0xAF,
'next_track':0xB0,  'previous_track':0xB1,
'stop_media':0xB2,  'play/pause_media':0xB3,
'start_mail':0xB4,  'select_media':0xB5,
'start_application_1':0xB6, 'start_application_2':0xB7,
'attn_key':0xF6,    'crsel_key':0xF7,   'exsel_key':0xF8,   'play_key':0xFA,    'zoom_key':0xFB,    'clear_key':0xFE,
';':0xBA,   '=':0xBB,   ',':0xBC,   '-':0xBD,   '.':0xBE,   '/':0xBF,   '`':0xC0,   '[':0xDB,   '\\':0xDC,  ']':0xDD,   "'":0xDE,   
}

VK_EXTEND_CODE = {
'space':    VK_BASIC_CODE['spacebar'], 
' ':        VK_BASIC_CODE['spacebar'], 

'Escape'    :VK_BASIC_CODE['esc'],

'Oem_3'     :VK_BASIC_CODE['`'],
# '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
'Oem_Minus' :VK_BASIC_CODE['-'],
'Oem_Plus'  :VK_BASIC_CODE['='],
'Back'      :VK_BASIC_CODE['backspace'],

'Tab'       :VK_BASIC_CODE['tab'],
'Q'         :VK_BASIC_CODE['q'],
'W'         :VK_BASIC_CODE['w'],
'E'         :VK_BASIC_CODE['e'],
'R'         :VK_BASIC_CODE['r'],
'T'         :VK_BASIC_CODE['t'],
'Y'         :VK_BASIC_CODE['y'],
'U'         :VK_BASIC_CODE['u'],
'I'         :VK_BASIC_CODE['i'],
'O'         :VK_BASIC_CODE['o'],
'P'         :VK_BASIC_CODE['p'],
'Oem_4'     :VK_BASIC_CODE['['],
'Oem_6'     :VK_BASIC_CODE[']'],
'Oem_5'     :VK_BASIC_CODE['\\'],

'Capital'   :VK_BASIC_CODE['caps_lock'],
'A'         :VK_BASIC_CODE['a'],
'S'         :VK_BASIC_CODE['s'],
'D'         :VK_BASIC_CODE['d'],
'F'         :VK_BASIC_CODE['f'],
'G'         :VK_BASIC_CODE['g'],
'H'         :VK_BASIC_CODE['h'],
'J'         :VK_BASIC_CODE['j'],
'K'         :VK_BASIC_CODE['k'],
'L'         :VK_BASIC_CODE['l'],
'Oem_1'     :VK_BASIC_CODE[';'],
'Oem_7'     :VK_BASIC_CODE["'"],
'Return'    :VK_BASIC_CODE['enter'],

'Lshift'    :VK_BASIC_CODE['left_shift'],
'Z'         :VK_BASIC_CODE['z'],
'X'         :VK_BASIC_CODE['x'],
'C'         :VK_BASIC_CODE['c'],
'V'         :VK_BASIC_CODE['v'],
'B'         :VK_BASIC_CODE['b'],
'N'         :VK_BASIC_CODE['n'],
'M'         :VK_BASIC_CODE['m'],
'Oem_Comma' :VK_BASIC_CODE[','],
'Oem_Period':VK_BASIC_CODE['.'],
'Oem_2'     :VK_BASIC_CODE['/'],
'Rshift'    :VK_BASIC_CODE['right_shift'],

'Lcontrol'  :VK_BASIC_CODE['left_control'],
'Lwin'      :0x5B,
'Lmenu'     :VK_BASIC_CODE['left_menu'],
'Space'     :VK_BASIC_CODE['spacebar'],
'Rmenu'     :VK_BASIC_CODE['right_menu'],
'Apps'      :VK_BASIC_CODE[' '],
'Rcontrol'  :VK_BASIC_CODE['right_control'],

'Home'      :VK_BASIC_CODE['home'],
'Prior'     :VK_BASIC_CODE['page_up'],
'Next'      :VK_BASIC_CODE['page_down'],
'End'       :VK_BASIC_CODE['end'],
'Left'      :VK_BASIC_CODE['left_arrow'],
'Up'        :VK_BASIC_CODE['up_arrow'],
'Right'     :VK_BASIC_CODE['right_arrow'],
'Down'      :VK_BASIC_CODE['down_arrow'],

# 'F1', 'F2', 'F3', 'F4', 'F5', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 
'Snapshot'  :VK_BASIC_CODE['print_screen'],
'Pause'     :VK_BASIC_CODE['pause'],
'Insert'    :VK_BASIC_CODE['ins'], 
'Delete'    :VK_BASIC_CODE['del'],
}


VK_CODE = {**VK_BASIC_CODE, **VK_EXTEND_CODE}