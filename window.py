import curses
import Settings
import time
import math
from windowManager import windowManager

class Window:
    def __init__(self, name: str, sizeY: int, sizeX: int, resize: bool):
        self.name = name
        # self.id = 1  # TODO: make an id system to assign unique ids
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.x = 0
        self.y = 0
        self.maxY = 0
        self.maxX = 0
        self.isBeingHeld = False
        self.isSnapped = False
        self.resizable = resize
        self.released = 0
        self.timeSinceReleased = 0
        self.setup()

    def setup(self):
        self.window = curses.newwin(self.sizeY, self.sizeX, 1, 1)
        self.maxY, self.maxX = self.window.getmaxyx()

    def updateWindow(self, my, mx, pressed, timeSinceReleased):
        self.window.border("|", "|", "-", "-", "+", "+","+","+")
        self.displayWindowTitle()
        self.window.refresh()
        
        self.processMoveAndSnap(my, mx, pressed)
        if(self.ifClickedInside(my, mx) and pressed):
            windowManager.focusWindow(self)
            
                
            
            
            

    def clear(self):
        self.window.clear()




    def moveWindow(self, newY, newX):
        newY, newX = self.validatePosition(newY,newX)
        self.window.mvwin(int(newY), int(newX))
        self.x = newX
        self.y = newY
        
        if(self.isSnapped):
            self.isSnapped = False
            self.resizeAfterUnsnap()
            
        
    def displayWindowTitle(self):
        self.window.addstr(0,0, self.name)
        
    def ifClickedInside(self, my,mx):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + self.maxX and mx >= self.x):
                return True
        return False
        

    def validatePosition(self, newY, newX):
        #thank you github copilot
        if newX + self.maxX > Settings.MAX_X:
            newX = Settings.MAX_X - self.maxX
        if newY + self.maxY > Settings.MAX_Y:
            newY = Settings.MAX_Y - self.maxY
        if newX < 0:
            newX = 0
        if newY < 0:
            newY = 0
        return newY, newX
        
    def resizeAfterUnsnap(self):
        self.maxX *= .5
        self.maxY *= .5
        math.ceil(self.maxX)
        math.ceil(self.maxY)
        self.window.resize(int(self.maxY), int(self.maxX))
    
    def snapToRightHalf(self, newY, newX, timeSinceReleased):
        #TODO: not nessecary but try and add the windows half opacity before snap so you know what your getting into
        
        #Snaps when you let go and your mouse is over the border
        # rightHalfCenterY, rightHalfCenterX = Settings.MAX_Y / 2, (Settings.MAX_X + Settings.MAX_X/2) /2
        currTime = time.time()
        if(not self.isBeingHeld and newX >= Settings.MAX_X - 1 and currTime - timeSinceReleased <= Settings.RELEASE_SNAPBUFFER):
            newY, newX = self.validatePosition(newY,newX)
            rightHalfCenterX = (Settings.MAX_X + Settings.MAX_X/2) / 2
            self.moveWindow(1, int(rightHalfCenterX - self.maxX/2))

            self.maxY = int(Settings.MAX_Y - 1)
            self.maxX = int(Settings.MAX_X /2)


            self.window.resize(self.maxY, self.maxX)
            self.clear()
            self.isSnapped = True
    
    
    def processMoveAndSnap(self,my,mx, pressed):
        """validatePosition If the proposed move is possible and do all things releated to the move
        """

        result = self.isTopBorder(my,mx,1)
        if(result or (self.isBeingHeld and pressed)):
            if(windowManager.isWindowHeld == self or windowManager.isWindowHeld is None):
                self.moveWindow(my,mx)
                self.isBeingHeld = True
                windowManager.isWindowHeld = self
                # self.released = time.time() 
        else:
            self.timeSinceReleased = time.time()
            self.isBeingHeld = False
            windowManager.isWindowHeld = None
            self.snapToRightHalf(my,mx, self.timeSinceReleased)
            
            
            
            
    
    
    
    def resizeWindow(self, newY, newX):
        pass

    
    
    
    def isTopBorder(self, my, mx, margin=0):
        if(my <= self.y + margin and my >= self.y):
            if(mx <= self.x + self.maxX and mx >= self.x):
                return True
        
    def isRightBorder(self, my, mx, margin=0):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + self.maxX + margin and mx >= self.x + self.maxX):
                return True
    
            

            
        