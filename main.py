import curses
from curses import wrapper
import InputManager
from window import Window
from windowManager import windowManager
import time
import Settings
import threading


timeSinceReleased = 0
released = time.time()



def init():
    stdscr = curses.initscr()
    
    stdscr.keypad(True)
    stdscr.nodelay(1)
    rows, cols = stdscr.getmaxyx()
    Settings.MAX_X = cols
    Settings.MAX_Y = rows
    
    curses.noecho()
    curses.nocbreak()
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    print('\033[?1003h')
    

# Function with the timer
def myTimer(seconds):
    while True:
        time.sleep(seconds)
        curses.flushinp()


def main(stdscr):
    global released
    my = 0
    mx = 0
    pressed = False
    

    stdscr.clear()
    

    test = Window("Test Window", 15, 20, True)
    test2 = Window("I Love Testing Windows", 10, 30, True)
    windowManager.addWindow(test)
    windowManager.addWindow(test2)

    
    myThread = threading.Thread(target=myTimer, args=(Settings.FLUSH_INPUT_INTERVAL,))
    myThread.start()
    
    while True:
        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        # TODO: Refresh on a need to basis
        stdscr.refresh()
        windowManager.update(my, mx, pressed, timeSinceReleased)
        # test.tick()


        key = stdscr.getch()


        if(key == curses.KEY_MOUSE):        
            _, mx, my, _, bstate = curses.getmouse()   
            if bstate == 2:
                pressed = True
            elif bstate == 1:
                pressed = False


        # get the window object if it is pressed on without looping?
        # Im thinking a way to get through this without programming all the windows is to give each objects "tick"
        # everything it needs to know like tick(my,mx,pressed,time) and have it do all its own proccesing for minimal
        # work in the main loop
        # if(pressed):
        #     result = test.isRightBorder(my,mx)
        #     if(result is True):
        #         test.move(my, mx)
        #         released = time.time()
        #         stdscr.clear()
        # else:
        #     timeSinceReleased = time.time()
        #     test.isBeingHeld = False
        #     test.snapToHalf(my, mx, timeSinceReleased)


        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break
        time.sleep(Settings.REFRESH_RATE)





init()
wrapper(main)



