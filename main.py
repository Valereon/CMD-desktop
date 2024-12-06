import curses
from curses import wrapper
import Settings.InputManager as InputManager
from Windows.window import Window
from Windows.windowManager import windowManager
import time
import Settings.Settings as Settings
from Windows.icon import Icon

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
    


def main(stdscr):
    global released
    my = 0
    mx = 0
    pressed = False
    

    stdscr.clear()
    

    test = Window("Test Window", 15, 20, True)
    test2 = Window("I Love Testing Windows", 10, 30, True)
    icon1 = Icon("Term", stdscr)
    windowManager.addWindow(test)
    windowManager.addWindow(test2)

    
    while True:
        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        # TODO: Refresh on a need to basis
        # i dont think its entierly necessary to refresh on a need to basis it doesnt seem to be impacting performance
        stdscr.refresh()
        icon1.displayIcon()
        windowManager.update(my, mx, pressed, timeSinceReleased)


        key = stdscr.getch()


        if(key == curses.KEY_MOUSE):        
            _, mx, my, _, bstate = curses.getmouse()   
            if bstate == 2:
                pressed = True
            elif bstate == 1:
                pressed = False
            elif bstate & curses.BUTTON1_DOUBLE_CLICKED:
                if(my == 5 and mx==5):
                    icon1.openProgam()

        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break
        time.sleep(Settings.REFRESH_RATE)





init()
wrapper(main)



