import curses
import time

from pynput import mouse

# from Components.window import Window
# from Windows.contextMenu import ContextMenu
# from Components.button import Button
from Windows.windowManager import windowManager
from Settings import InputManager, Settings
from Windows.desktop import desktop
from Components.icon import Icon
from Data import GlobalVars as GV
from Windows.taskbar import Taskbar
from CustomContent import CustomContent
from Data import Apps

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
    GV.stdscr = stdscr
    CustomContent.main()


def main(stdscr):
    global pressed, released


    stdscr.erase()

    # icon1 = Icon("Term", stdscr, [".____", r"|>\  |", "|____|"], 11, 10)
    # icon2 = Icon("Term", stdscr, 11, 20)
    # icon3 = Icon("Term", stdscr, 11, 12)
    # icon4 = Icon("Term", stdscr, 15, 13)
    icon5 = Icon("Term", stdscr, ["Balls", "Balls", "Balls"], Apps.REGISTERED_APPS[0],10, 10)
    
    # desktop.icons.append(icon1)
    # desktop.icons.append(icon2)
    # desktop.icons.append(icon3)
    # desktop.icons.append(icon4)
    desktop.icons.append(icon5)


    
    # button1 = Button("yo man", coolFunction)
    # button2 = Button("")
    # button3 = Button("yman")
    # button4 = Button("")
    
    # options = [button1, button2, button3, button4]
    
    # menu = ContextMenu(options,15, 10, 20)
    
    taskbar = Taskbar()
    
    icon6 = Icon("", taskbar.window, ["CMD", "DSKTP"], 1, 1)
    icon7 = Icon("", taskbar.window, ["INT", "ERNET"], 1, 7)   
    
    
    # taskbar.addIcon(icon6)
    # taskbar.addIcon(icon7)
    
    
    
    
    while True:
        key = stdscr.getch() 
        stdscr.erase()
        stdscr.border("|", "|", "-", "-", "+", "+", "+", "+")
        desktop.update()
        windowManager.update()
        stdscr.noutrefresh() 
        #ANYTHING THAT IS IN FRONT OF THE DESKTOP SHOULD STAGE REFRESH BELOW
        taskbar.update()

        
        
        

        curses.doupdate() # ORDER MATTERS FOR screen.noutrefresh

        if(key == curses.KEY_MOUSE):
            _, GV.mouseX, GV.mouseY, _, GV.cursesBState = curses.getmouse()
            if(curses.BUTTON1_DOUBLE_CLICKED): # need to find a condiotn to make this true only when clicking
                GV.wasDoubleClicked = True
            else:
                GV.wasDoubleClicked = False
            
            
            if(GV.cursesBState and curses.BUTTON1_PRESSED):
                GV.isMouse1Pressed = True
            elif(GV.cursesBState and curses.BUTTON1_RELEASED):
                GV.isMouse1Pressed = False
            
            


    
                
        result = InputManager.keyDo(key,stdscr)
        if(result == "break"):
            break

        time.sleep(Settings.REFRESH_RATE)





init()



def on_click(x, y, button, isPressed):
    GV.isMouse0Pressed = isPressed




with mouse.Listener(on_click=on_click) as listener:
    curses.wrapper(main)
