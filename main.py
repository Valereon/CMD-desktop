import curses
import time

from pynput import mouse

from Windows.windowManager import windowManager
from Settings import InputManager, Settings
from Windows.desktop import desktop
from Windows.icon import Icon
from Windows.contextMenu import ContextMenu
from Settings import GlobalVars as GV

timeSinceReleased = 0
released = time.time()



def init():
    stdscr = curses.initscr()
    stdscr.keypad(True)
    stdscr.nodelay(1)
    stdscr.idcok(False)
    stdscr.idlok(False)
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

    icon1 = Icon("Term", stdscr, 11, 10)
    icon2 = Icon("Term", stdscr, 11, 20)
    icon3 = Icon("Term", stdscr, 11, 12)
    icon4 = Icon("Term", stdscr, 15, 13)
    icon5 = Icon("Term", stdscr, 10, 14)
    
    desktop.icons.append(icon1)
    desktop.icons.append(icon2)
    desktop.icons.append(icon3)
    desktop.icons.append(icon4)
    desktop.icons.append(icon5)
    
    menu = ContextMenu("Blah",20, 20, 20)
    
    while True:
        # stdscr.border("|", "|", "-", "-", "+", "+", "+", "+")
        # TODO: Refresh on a need to basis
        # i dont think its entirely necessary to refresh on a need to basis it doesn't seem to be impacting performance
        key = stdscr.getch() # this is the issue with the flickering bc moving the mouse calls a refresh i think
        stdscr.erase()
        desktop.update()
        menu.update()
        # windowManager.update()
        stdscr.noutrefresh()
        
        curses.doupdate()


        if(key == curses.KEY_MOUSE):
            _, GV.mouseX, GV.mouseY, _, GV.cursesBState = curses.getmouse()
            if GV.cursesBState & curses.BUTTON1_DOUBLE_CLICKED:
                GV.wasDoubleClicked = True
            else:
                GV.wasDoubleClicked = False

        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break

        time.sleep(Settings.REFRESH_RATE)





init()



def on_click(x, y, button, isPressed):
    GV.isMousePressed = isPressed




with mouse.Listener(on_click=on_click) as listener:
    curses.wrapper(main)
