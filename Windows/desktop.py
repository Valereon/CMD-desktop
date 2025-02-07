from Windows.windowManager import windowManager
from Settings import GlobalVars as GV


class Desktop:
    def __init__(self):
        self.icons = []
        self.isIconHeld = False
        self.currentHeldIcon = None
    
    def update(self):
        for i in self.icons:
            i.displayIcon()
        self.checkIcons()
    
    
    def checkIcons(self):
        if (windowManager.focusedWindow is None):
            self.isIconHovered(GV.mouseY,GV.mouseX)
    
    def isIconHovered(self, y, x):
        for i in self.icons:
            i.isHovered()
        




desktop = Desktop()