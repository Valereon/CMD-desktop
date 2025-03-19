import curses
from Components.entity import Entity
from Data import GlobalVars as GV
from Windows.desktop import desktop
from Windows.windowManager import windowManager


class Icon(Entity):
    def __init__(self, name, win, iconText, programToOpen, y=10, x=10):
        # TODO: add a arg to add a programtoopen
        # TODO: add a way to specify icon text and look
        self.win = win
        self.name = name
        self.programToOpen = programToOpen
        # self.programToOpenArgs = [self.name, Settings.DEFAULT_WINDOW_Y, Settings.DEFAULT_WINDOW_X, False]
        self.iconText = iconText
        self.maxX = len(self.iconText[0])
        self.maxY = len(self.iconText)
        super().__init__(name, self.maxX, self.maxY)
        self.x = x
        self.y = y
        self.displayAttribute = curses.A_NORMAL
        self.getGlobalCoordinates(self.win)

    # def init(self, win):
    #     self.getGlobalCoordinates(win)

    def update(self):
        """IS ONLY CALLED IF ICON IS HOVERED"""
        # FIXME: This is a cooked way to do it but whatever
        if(not self.displayAttribute == curses.A_BOLD):
            return
        
        # self.isClicked()
        if(GV.wasDoubleClicked):
            print(GV.wasDoubleClicked)
            self.openProgram()
        
        if(GV.isMouse0Pressed):
            if(desktop.isIconHeld == False or desktop.currentHeldIcon == self):
                desktop.isIconHeld = True
                desktop.currentHeldIcon = self
                self.moveIcon()
        else:
            desktop.isIconHeld = False
            desktop.currentHeldIcon = None
        

    def openProgram(self):
        if(self.programToOpen is not None):
            windowManager.addWindow(self.programToOpen())

    def isHovered(self, useGlobal=False):
        # this is for if the icon is being held but the mouse is not inside its bounds it wont follow it when moving
            
        if(desktop.currentHeldIcon == self):
            self.update()
        
        if(not self.isPointInside(GV.mouseY,GV.mouseX, useGlobal)):
            self.displayAttribute = curses.A_NORMAL
            return

        self.displayAttribute = curses.A_BOLD
        
        
        self.update()
        
    
    def isClicked(self, useGlobal=False):
        # since the icon only when hovered you dont need to check pos
        #BUG: the mouse pressing is only long press like wtf
        if(GV.isMouse0Pressed):    
            self.openProgram()

    def moveIcon(self):
        self.y, self.x = self.validatePosition(GV.mouseY, GV.mouseX)


    def displayIcon(self):
        for i in range(len(self.iconText)):
            self.win.addstr(self.y + i, self.x, self.iconText[i], self.displayAttribute)
            
        if(self.name == ""):
            return
        self.win.addstr(self.y + self.maxY, self.x, self.name, self.displayAttribute)
