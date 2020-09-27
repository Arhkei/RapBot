import ctypes
import time
import random

w = 0x11
s = 0x1F
q = 0x10
e = 0x12
r = 0x13
t = 0x14
y = 0x15
u = 0x16
i = 0x17
o = 0x18
p = 0x19
a = 0x1E
d = 0x20
f = 0x21
g = 0x22
h = 0x23
j = 0x24
k = 0x25
l = 0x26
z = 0x2C
x = 0x2D
c = 0x2E
v = 0x2F
b = 0x30
n = 0x31
m = 0x32
num1 = 0x02
num2 = 0x03
num3 = 0x04
num4 = 0x05
num5 = 0x06
num6 = 0x07
num7 = 0x08
num8 = 0x09
num9 = 0x0A
num0 = 0x0B
slash = 0x35
space = 0x39
enter = 0x1C
shift = 0x2A
comma = 0x33
apostrophe = 0x28
period = 0x34
SendInput = ctypes.windll.user32.SendInput

# Raps graciously brought to you by some random rap forums I found

RapBank = []

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    xa = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(xa), ctypes.sizeof(xa))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(xa), ctypes.sizeof(xa))

def Type(sentence):
    time.sleep(.3)
    PressKey(slash)
    time.sleep(.3)
    for xy in sentence:
        if xy == " ":
            PressKey(space)
        elif xy == ",":
            PressKey(comma)
        elif xy == "'":
            PressKey(apostrophe)
        elif xy == ".":
            PressKey(period) 
        elif xy == "a":
            PressKey(a)
        elif xy == "b":
            PressKey(b)
        elif xy == "c":
            PressKey(c)
        elif xy == "d":
            PressKey(d)
        elif xy == "e":
            PressKey(e)
        elif xy == "f":
            PressKey(f)
        elif xy == "g":
            PressKey(g)
        elif xy == "h":
            PressKey(h)
        elif xy == "i":
            PressKey(i)
        elif xy == "j":
            PressKey(j)
        elif xy == "k":
            PressKey(k)
        elif xy == "l":
            PressKey(l)
        elif xy == "m":
            PressKey(m)
        elif xy == "n":
            PressKey(n)
        elif xy == "o":
            PressKey(o)
        elif xy == "p":
            PressKey(p)
        elif xy == "q":
            PressKey(q)
        elif xy == "r":
            PressKey(r)
        elif xy == "s":
            PressKey(s)
        elif xy == "t":
            PressKey(t)
        elif xy == "u":
            PressKey(u)
        elif xy == "v":
            PressKey(v)
        elif xy == "w":
            PressKey(w)
        elif xy == "x":
            PressKey(x)
        elif xy == "y":
            PressKey(y)
        elif xy == "z":
            PressKey(z)
        elif xy == "A":
            PressKey(shift)
            PressKey(a)
            ReleaseKey(shift)
        elif xy == "B":
            PressKey(shift)
            PressKey(b)
            ReleaseKey(shift)
        elif xy == "C":
            PressKey(shift)
            PressKey(c)
            ReleaseKey(shift)
        elif xy == "D":
            PressKey(shift)
            PressKey(d)
            ReleaseKey(shift)
        elif xy == "E":
            PressKey(shift)
            PressKey(e)
            ReleaseKey(shift)
        elif xy == "F":
            PressKey(shift)
            PressKey(f)
            ReleaseKey(shift)
        elif xy == "G":
            PressKey(shift)
            PressKey(g)
            ReleaseKey(shift)
        elif xy == "H":
            PressKey(shift)
            PressKey(h)
            ReleaseKey(shift)
        elif xy == "I":
            PressKey(shift)
            PressKey(i)
            ReleaseKey(shift)
        elif xy == "J":
            PressKey(shift)
            PressKey(j)
            ReleaseKey(shift)
        elif xy == "K":
            PressKey(shift)
            PressKey(k)
            ReleaseKey(shift)
        elif xy == "L":
            PressKey(shift)
            PressKey(l)
            ReleaseKey(shift)
        elif xy == "M":
            PressKey(shift)
            PressKey(m)
            ReleaseKey(shift)
        elif xy == "N":
            PressKey(shift)
            PressKey(n)
            ReleaseKey(shift)
        elif xy == "O":
            PressKey(shift)
            PressKey(o)
            ReleaseKey(shift)
        elif xy == "P":
            PressKey(shift)
            PressKey(p)
            ReleaseKey(shift)
        elif xy == "Q":
            PressKey(shift)
            PressKey(q)
            ReleaseKey(shift)
        elif xy == "R":
            PressKey(shift)
            PressKey(r)
            ReleaseKey(shift)
        elif xy == "S":
            PressKey(shift)
            PressKey(s)
            ReleaseKey(shift)
        elif xy == "T":
            PressKey(shift)
            PressKey(t)
            ReleaseKey(shift)
        elif xy == "U":
            PressKey(shift)
            PressKey(u)
            ReleaseKey(shift)
        elif xy == "V":
            PressKey(shift)
            PressKey(v)
            ReleaseKey(shift)
        elif xy == "W":
            PressKey(shift)
            PressKey(w)
            ReleaseKey(shift)
        elif xy == "X":
            PressKey(shift)
            PressKey(x)
            ReleaseKey(shift)
        elif xy == "Y":
            PressKey(shift)
            PressKey(y)
            ReleaseKey(shift)
        elif xy == "Z":
            PressKey(shift)
            PressKey(z)
            ReleaseKey(shift)
        elif xy == "?":
            PressKey(shift)
            PressKey(slash)
            ReleaseKey(shift)
        elif xy == "1":
            PressKey(num1)
        elif xy == "2":
            PressKey(num2)
        elif xy == "3":
            PressKey(num3)
        elif xy == "4":
            PressKey(num4)
        elif xy == "5":
            PressKey(num5)
        elif xy == "6":
            PressKey(num6)
        elif xy == "7":
            PressKey(num7)
    time.sleep(.3)
    PressKey(enter)
    
def randomRap():
    time.sleep(.3)
    randNum = random.randint(0,len(RapBank)-1)
    return(Type(RapBank[randNum]))
# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
time.sleep(3)
randomRap()
randomRap()
randomRap()
randomRap()
randomRap()
randomRap()
randomRap()


