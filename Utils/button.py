import curses
from Settings import GlobalVars as GV
from entity import Entity
class Button(Entity):
    def __init__(self, text, highlight=curses.A_BOLD, nonHighlight=curses.A_NORMAL, func=None):
        self.text = text
        self.highlight = highlight
        self.nonHighlight = nonHighlight
        self.func = func
        
        self.globalY = 0
        self.globalX = 0
        super().__init__(text, len(text), 1)
        

    def press(self, args=None):
        if(args is None):
            self.func()
        else:
            self.func(args)
            
            
    def display(self,stdscr, y,x):
        isInside = self.isPointInside(GV.mouseY, GV.mouseX)
        if(isInside):
            stdscr.addstr(y,x, self.text, self.highlight)
        else:
            stdscr.addstr(y,x, self.text, self.nonHighlight)
        
    def setGlobalYX(self, y,x):
        self.y = y
        self.x = x