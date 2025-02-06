import curses
from Windows import window
from entity import Entity
from Settings import Settings
from Windows.windowManager import windowManager
from Settings import GlobalVars as GV


class Icon(Entity):
    def __init__(self, name, win, y=10, x=10):
        # TODO: add a arg to add a programtoopen
        # TODO: add a way to specify icon text and look
        self.win = win
        self.name = name
        self.programToOpen = window
        self.programToOpenArgs = [self.name, Settings.DEFAULT_WINDOW_Y, Settings.DEFAULT_WINDOW_X, False]
        self.iconText = [".____", r"|>\  |", "|____|"]
        self.maxX = len(self.iconText[0])
        self.maxY = len(self.iconText)
        super().__init__(name, self.maxX, self.maxY)
        self.x = 5
        self.y = 5
        self.displayAttribute = curses.A_NORMAL


    def update(self):
        """IS ONLY CALLED IF ICON IS HOVERED"""
        # FIXME: This is a cooked way to do it but whatever
        if(self.displayAttribute == curses.A_BOLD):
            self.isClicked()
            


    def openProgram(self):
        windowManager.addWindow(self.programToOpen(*self.programToOpenArgs))

    def isHovered(self):
        self.update()
        if(not self.isPointInside(GV.mouseY,GV.mouseX)):
            self.displayAttribute = curses.A_NORMAL
            return
        self.displayAttribute = curses.A_BOLD
        
        
    
    def isClicked(self):
        if(self.isPointInside(GV.mouseY,GV.mouseX) and doubleclicked):
            raise("FUCK")
            # self.openProgram()

    def moveIcon(self, y, x):
        #TODO: Implement this
        self.win.clear()


    def displayIcon(self):
        for i in range(len(self.iconText)):
            self.win.addstr(self.y + i, self.x, self.iconText[i], self.displayAttribute)
        self.win.addstr(self.y + self.maxY, self.x, self.name, self.displayAttribute)
