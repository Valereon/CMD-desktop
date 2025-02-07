# the plan
# have a text object for the menu
# find some way to display it maybe 
# 1. make another window inside of the screen like how the windows are done
# 2. just display the text over the other stuff and refresh when it closes the context menu
# Find out how to detect menu decisions
# 1. hand make every context menu to be special
# 2. just make them on an adjustable grid like 13x5 so 13 characters long and 5 items

# also would like to do the bold highlighting i did on the icons when you hover
# add some built in context menu style

import curses
import time
from Settings import Settings
class ContextMenu():
    def __init__(self, menuText, width, height, colAmount):
        self.menuText = menuText
        self.width = width
        self.height = height
        self.colAmount = colAmount
        self.style = None
        self.menuOptions = ["New Folder", "New Txt File", "New bull","ergreg","new new"] # this is so you can call methods i guess probably have a return call from a method
        self.needsRedraw = True
        
        self.window = curses.newwin(self.height, self.width, 5, 5)
        self.maxY, self.maxX = self.window.getmaxyx()
        self.window.nodelay(1)
        self.window.keypad(True)
    
    def update(self):
        if self.needsRedraw:
            self.window.erase()
            self.window.border("|", "|", "-", "-", "+", "+","+","+")
            self.display()
            self.window.noutrefresh()
            self.needsRedraw = False
        
        
    
    
    
    def display(self):
    # Exclude top and bottom border from available drawing space
        inner_height = self.height - 2
        segment = inner_height / self.colAmount
        for index in range(self.colAmount):
            vertical_position = 1 + int((index + 0.5) * segment)
            for x in range(0, self.maxX - 1):
                self.window.addstr(vertical_position, x, "-")
            if index < len(self.menuOptions):
                self.window.addstr(vertical_position, 1, self.menuOptions[index])


        

        