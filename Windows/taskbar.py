# The plan
# make a window with a specific height of like 10 and the width of the screen
# make little icons like the icons on the desktop
# lock them to the x axis 
# make other icons slide out of the way if one is hovering on top 
# make them get a window that was previously put

from entity import Entity
import curses
from Settings import Settings

class Taskbar(Entity):
    def __init__(self):
        self.icons = []
        
        super().__init__("TaskBar", Settings.TASKBAR_HEIGHT, Settings.TASKBAR_WIDTH)
        self.window = curses.newwin(Settings.TASKBAR_HEIGHT, Settings.TASKBAR_WIDTH, Settings.MAX_Y - Settings.TASKBAR_HEIGHT + Settings.TASKBAR_OFFSET_Y, 0 + Settings.TASKBAR_OFFSET_X)
        self.maxY, self.maxX = self.window.getmaxyx()
    
    def update(self):
        self.window.erase()
        self.window.border("|", "|", "-", "-", "+", "+", "+", "+")
        self.window.noutrefresh()
    
    
    
        
    def addIcon():
        pass
    
    