from entity import Entity
from Windows.windowManager import windowManager
from Windows.window import Window

class Icon(Entity):
    def __init__(self, name, win):
        self.win = win
        self.name = name
        self.programToOpen = Window
        self.progamToOpenArgs = [self.name, 10, 10, False]
        self.iconText = [".____", "|>\  |", "|____|"]
        self.maxX = len(self.iconText[0])
        self.maxY = len(self.iconText)
        super().__init__(name, self.maxX, self.maxY)
        self.x = 5
        self.y = 5
    
    def openProgam(self):
        windowManager.addWindow(self.programToOpen(*self.progamToOpenArgs))
        
    
    
    def moveIcon(self, y, x):
        self.moveEntity(y,x)
        self.win.clear()
        
        
    def displayIcon(self):
        for i in range(len(self.iconText)):
            self.win.addstr(self.y + i, self.x, self.iconText[i])
        self.win.addstr(self.y + self.maxY, self.x, self.name)
        