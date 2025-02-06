from Windows.windowManager import windowManager
from Settings import GlobalVars as GV


class Desktop:
    def __init__(self):
        self.icons = []
    
    def update(self):
        pass
    
    
    def checkIcons(self):
        if (windowManager.focusedWindow is None):
            self.isIconHovered(GV.mouseY,GV.mouseX)
    
    def isIconHovered(self, y, x):
        for i in self.icons:
            i.isHovered()
        




desktop = Desktop()