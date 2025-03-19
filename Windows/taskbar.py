# The plan
# make a window with a specific height of like 10 and the width of the screen
# make little icons like the icons on the desktop
# lock them to the x axis 
# make other icons slide out of the way if one is hovering on top 
# make them get a window that was previously put

from Components.entity import Entity
import curses
from Settings import Settings

class Taskbar(Entity):
    def __init__(self):
        self.icons = []
        
        super().__init__("TaskBar", Settings.TASKBAR_HEIGHT, Settings.TASKBAR_WIDTH)
        self.window = curses.newwin(Settings.TASKBAR_HEIGHT, Settings.TASKBAR_WIDTH, Settings.MAX_Y - Settings.TASKBAR_HEIGHT + Settings.TASKBAR_OFFSET_Y, 0 + Settings.TASKBAR_OFFSET_X)
        self.maxY, self.maxX = self.window.getmaxyx()
        self.window.keypad(True)
        self.window.nodelay(1)
    
    def init(self):
        for i in self.icons:
            i.getGlobalCoordinates(self.window)
    
    def update(self):
        self.window.erase()
        self.window.border("|", "|", "-", "-", "+", "+", "+", "+")

        # icon.update() will return true if its being hovered and null if its not
        # also to prevent more code this just locks it on the y axis and should be good
        for i in self.icons:
            i.displayIcon()
            i.isHovered(True)
            # self.updateIcon(i)
        
        self.window.noutrefresh()
    
    # def updateIcon(self, icon):
    #     icon.y = Settings.MAX_Y - Settings.TASKBAR_HEIGHT + Settings.TASKBAR_OFFSET_Y - icon.


        
    def addIcon(self, icon):
        self.icons.append(icon)
    
    