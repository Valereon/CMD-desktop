import curses
from curses import wrapper
import InputManager
from window import Window
import time
import Settings

stdscr = curses.initscr()
curses.noecho()
curses.nocbreak()
stdscr.keypad(True)
curses.mousemask(curses.BUTTON1_PRESSED | curses.BUTTON1_RELEASED | curses.BUTTON1_CLICKED | curses.REPORT_MOUSE_POSITION)
print('\033[?1003h')

timeSinceReleased = 0
released = time.time()

rows, cols = stdscr.getmaxyx()

Settings.MAX_X = cols
Settings.MAX_Y = rows


def main(stdscr):
    global released
    mx = 0
    my = 0
    pressed = False


    stdscr.clear()
    test = Window("Test Window", 10, 20, True)
    
    stdscr.nodelay(1)
    while True:
        stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
        #TODO: Refresh a need to basis
        stdscr.refresh()
        test.tick()


        key = stdscr.getch()




        if(pressed):
            # test.topBorder(my,mx)
            # if(test.isBeingHeld is True):
            test.move(my, mx)
            # released = time.time()
                
        # else:
            # timeSinceReleased = time.time()
            # stdscr.addstr(10,10, str(timeSinceReleased - released))
            
            # test.isBeingHeld = False
            # test.snapToHalf(my, mx, timeSinceReleased)


        if(key == curses.KEY_MOUSE):        
            _, mx, my, _, bstate = curses.getmouse()   
            if bstate == 2:
                pressed = True
            elif bstate == 1:
                pressed = False
            


            
        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break
        time.sleep(Settings.REFRESH_RATE)






wrapper(main)








def endWindow():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
