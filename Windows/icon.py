from entity import Entity
from Settings import Settings
from Windows.window import Window
from Windows.windowManager import windowManager


class Icon(Entity):
    def __init__(self, name, win):
        self.win = win
        self.name = name
        self.programToOpen = Window
        self.progamToOpenArgs = [self.name, Settings.DEFAULT_WINDOW_Y, Settings.DEFAULT_WINDOW_X, False]
        self.iconText = [".____", r"|>\  |", "|____|"]
        self.maxX = len(self.iconText[0])
        self.maxY = len(self.iconText)
        super().__init__(name, self.maxX, self.maxY)
        self.x = 5
        self.y = 5

    def openProgam(self):
        windowManager.addWindow(self.programToOpen(*self.progamToOpenArgs))



    def moveIcon(self, y, x):
        self.win.clear()


    def displayIcon(self):
        for i in range(len(self.iconText)):
            self.win.addstr(self.y + i, self.x, self.iconText[i])
        self.win.addstr(self.y + self.maxY, self.x, self.name)
