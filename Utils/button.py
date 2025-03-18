import curses
from Settings import GlobalVars as GV
from entity import Entity
class Button(Entity):
    def __init__(self, text, func=None, highlight=curses.A_BOLD, nonHighlight=curses.A_NORMAL):
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

        #BUG: you have to press and hold for this to work you cannot click
        if(isInside and GV.isMouse0Pressed and self.func is not None):
            self.press()
        
        if(isInside):
            stdscr.addstr(y,x, self.text, self.highlight)
        else:
            stdscr.addstr(y,x, self.text, self.nonHighlight)
        
    def setGlobalYX(self, y, x):
        self.y = y
        self.x = x