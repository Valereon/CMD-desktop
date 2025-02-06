import curses
import time

from pynput import mouse

from Windows.windowManager import windowManager
from Settings import InputManager, Settings
from Windows.desktop import desktop
from Windows.icon import Icon
from Settings import GlobalVars as GV

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
    curses.curs_set(0)
    curses.nocbreak()
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    print("\033[?1003h")



def main(stdscr):
    global pressed, released


    stdscr.erase()

    icon1 = Icon("Term", stdscr, 10, 10)
    desktop.icons.append(icon1)

    while True:
        stdscr.border("|", "|", "-", "-", "+", "+", "+", "+")
        # TODO: Refresh on a need to basis
        # i dont think its entirely necessary to refresh on a need to basis it doesn't seem to be impacting performance
        key = stdscr.getch() # this is the issue with the flickering bc moving the mouse calls a refresh i think
        stdscr.clear()
        icon1.displayIcon()
        windowManager.update()

        #TODO: this checks all of the icons every frame, i dont actually know how inefficient this is oh well
        desktop.checkIcons()



        if(key == curses.KEY_MOUSE):
            _, GV.mouseX, GV.mouseY, _, GV.cursesBstate = curses.getmouse()
            if GV.cursesBstate & curses.BUTTON1_DOUBLE_CLICKED:
                if(windowManager.focusedWindow is None):
                    pass


        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break
        time.sleep(Settings.REFRESH_RATE)





init()



def on_click(x, y, button, isPressed):
    GV.isMousePressed = isPressed




with mouse.Listener(on_click=on_click) as listener:
    curses.wrapper(main)
