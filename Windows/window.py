import curses
import Settings.Settings as Settings
import time
import math
from Windows.windowManager import windowManager
from entity import Entity

class Window(Entity):
    def __init__(self, name: str, sizeY: int, sizeX: int, resize: bool):
        # self.id = 1  # TODO: make an id system to assign unique ids
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.isBeingHeld = False
        self.isSnapped = False
        self.resizable = resize
        self.released = 0
        self.timeSinceReleased = 0
        self.setup()
        super().__init__(name, self.maxX, self.maxY)

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

    def move(self):
        self.window.mvwin(self.y, self.x)
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
            self.moveEntity(1, int(rightHalfCenterX - self.maxX/2))
            self.move()

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
                self.moveEntity(my,mx)
                self.move()
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
    
            

            
        