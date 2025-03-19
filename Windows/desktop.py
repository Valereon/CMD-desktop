from Windows.windowManager import windowManager
from Data import GlobalVars as GV


class Desktop:
    def __init__(self):
        self.icons = []
        self.isIconHeld = False
        self.currentHeldIcon = None
    
    def update(self):
        for i in self.icons:
            i.displayIcon()
            if (windowManager.focusedWindow is None):
                i.isHovered()
        




desktop = Desktop()