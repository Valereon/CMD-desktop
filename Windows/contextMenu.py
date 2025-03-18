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
from entity import Entity


class ContextMenu(Entity):
    """A Configurable context menu"""
    def __init__(self, menuOptions, width, height, colAmount, y=5,x=5):
        """
            (Button) Menu Options: The options you want for your menu
            (int) width: width of the menu
            (int) height: height of the menu
            (int) colAmount: how many columns long is the menu
            (Internal) Style: haven't implemented but will be different border types for the menu
        """
        # self.menuText = menuText
        self.width = width
        self.height = height
        self.colAmount = colAmount
        self.style = None
        self.menuOptions = menuOptions
        self.y = y
        self.x = x
        self.window = curses.newwin(self.height, self.width, 5, 5)
        self.maxY, self.maxX = self.window.getmaxyx()
        super().__init__("",self.maxX,self.maxY)
        self.setButtons()
    
    def update(self):
        self.window.erase()
        self.window.border("|", "|", "-", "-", "+", "+","+","+")
        self.display()
        self.window.noutrefresh()
    
    
    def setButtons(self):
        for i in range(len(self.menuOptions)):
            self.menuOptions[i].setGlobalYX(5,5)
        
    
    
    def display(self):
        inner_height = self.height - 2
        segment = inner_height / self.colAmount
        for index in range(self.colAmount):
            vertical_position = 1 + int((index + 0.5) * segment)
            # Start horizontal line from column 1 to preserve left border
            for x in range(1, self.maxX - 1):
                self.window.addstr(vertical_position, x, "-")

        # Display buttons with correct positioning
        for i, button in enumerate(self.menuOptions):
            button_y = 5 + i + 1
            button_x = 5 + 1
            button.setGlobalYX(button_y, button_x)
            button.display(self.window, i + 1, 1)
            