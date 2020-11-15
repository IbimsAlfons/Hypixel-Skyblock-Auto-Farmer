from pynput.keyboard import Key, Listener
from _thread import *
from pynput.mouse import Button, Controller
import ctypes
import time
import os


mouse = Controller()

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
UP = 0xC8
LEFT = 0xCB
RIGHT = 0xCD
DOWN = 0xD0
ENTER = 0x1C
ESC = 0x01
TWO = 0x03

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
                ("time", ctypes.c_ulong),
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
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# directx scan codes
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html


def Stop():
    def stop_(key):
        if str(key.char)=="i" or str(key.char)=="I":
            print("lol")
            #interrupt_main()
            ReleaseKey(W)
            ReleaseKey(A)
            ReleaseKey(D)
            ReleaseKey(S)
            mouse.release(Button.left)
            os._exit(0)
            
    with Listener(on_press=stop_) as listener:
        listener.join()

if __name__ == '__main__':
    time.sleep(4)
    start_new_thread(Stop, ())
    while (True):
        #time.sleep(4)
        PressKey(0x11)
        PressKey(0x1E)
        mouse.press(Button.left)
        time.sleep(20)
        mouse.release(Button.left)
        ReleaseKey(0x1E)
        ReleaseKey(0x11)
        mouse.move(10000,0) #x, y
        time.sleep(0.4)
        #############
        PressKey(0x11)
        time.sleep(0.6)
        ReleaseKey(0x11)
        mouse.move(80000,0) #x, y
        time.sleep(0.1)
        mouse.move(80000,0) #x, y

        ################################# WORK
        #time.sleep(4)
        PressKey(0x11)
        PressKey(0x20)
        mouse.press(Button.left)
        time.sleep(20)
        mouse.release(Button.left)
        ReleaseKey(0x20)
        ReleaseKey(0x11)
        mouse.move(-10000,0) #x, y
        time.sleep(0.4)
        #############
        PressKey(0x11)
        time.sleep(0.6)
        ReleaseKey(0x11)
        mouse.move(-80000,0) #x, y
        time.sleep(0.1)
        mouse.move(-80000,0) #x, y
        time.sleep(0.4)
        #break
