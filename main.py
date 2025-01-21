import curses
import time

from pynput import mouse

from Settings import InputManager, Settings
from Windows.icon import Icon
from Windows.windowManager import windowManager

timeSinceReleased = 0
released = time.time()
pressed = False



def init():
    stdscr = curses.initscr()

    stdscr.keypad(True)
    stdscr.nodelay(1)
    rows, cols = stdscr.getmaxyx()
    Settings.MAX_X = cols
    Settings.MAX_Y = rows

    curses.noecho()
    curses.curs_set(0)
    curses.nocbreak()
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    print("\033[?1003h")



def main(stdscr):
    global pressed, released
    my = 0
    mx = 0


    stdscr.erase()

    icon1 = Icon("Term", stdscr)

    while True:
        stdscr.border("|", "|", "-", "-", "+", "+", "+", "+")
        # TODO: Refresh on a need to basis
        # i dont think its entierly necessary to refresh on a need to basis it doesnt seem to be impacting performance
        key = stdscr.getch() # this is the issue with the flickering bc moving the mouse calls a refresh
        stdscr.clear()
        icon1.displayIcon()
        windowManager.update(my, mx, pressed)




        if(key == curses.KEY_MOUSE):
            _, mx, my, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_DOUBLE_CLICKED:
                if(my == 5 and mx==5):
                    icon1.openProgam()

        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break
        time.sleep(Settings.REFRESH_RATE)





init()



def on_click(x, y, button, isPressed):
    global pressed
    pressed = isPressed




with mouse.Listener(on_click=on_click) as listener:
    curses.wrapper(main)
