import curses
import math
import time

from entity import Entity
from Settings import Settings
from Windows.windowManager import windowManager


class Window(Entity):
    """The window class for all windows, they can be resized moved minimized and maximized as you would expect from a window"""
    def __init__(self, name: str, sizeY: int, sizeX: int, resize: bool):
        #self.id = 1  # TODO: make an id system to assign unique ids  # noqa: ERA001
        self.sizeY = sizeY
        self.sizeX = sizeX
        self.finalY = sizeY
        self.finalX = sizeX
        
        self.isBeingHeld = False
        self.isBeingResized = False
        self.isSnapped = False
        self.resizable = resize
        
        self.released = 0
        self.timeSinceReleased = 0

        self.window = curses.newwin(self.sizeY, self.sizeX, 1, 1)
        self.maxY, self.maxX = self.window.getmaxyx()

        super().__init__(name, self.maxX, self.maxY)

    def updateWindow(self, my, mx, pressed):
        """This is the windows ticks an update every Settings.REFRESH_RATE"""
        self.window.border("|", "|", "-", "-", "+", "+","+","+")
        # self.displayWindowTitle()
        self.window.refresh()
        self.ceilCoordsNScale()

        if(self.isTopBorder(my,mx,1) or self.isBeingHeld):
            self.checkAndMove(my,mx,pressed)
        
        if(self.isRightBorder(my,mx,1) or self.isBeingResized):
            self.resizeWindow(self.maxY,mx + self.maxX -12, pressed)  # for some reason there is a weird scaling offset idk what causes it or how to fix it
            self.window.erase()
            
        if(self.ifClickedInside(my, mx) and pressed):
            windowManager.focusWindow(self)
            

    def ceilCoordsNScale(self):
        """Math.ceils the coordinates and scale because of math producing floating points and curses cannot handle floating point scale and position
        """
        self.x = math.ceil(self.x)
        self.y = math.ceil(self.y)
        self.maxX = math.ceil(self.maxX)
        self.maxY = math.ceil(self.maxY)

    def WindowCoordsToMouseCoords(self,my,mx):
        self.y = my
        self.x = mx

    def clear(self):
        self.window.clear()

    def displayWindowTitle(self):
        self.window.addstr(0,0, self.name)
        # TODO: Fix this window minimize x and maximize
        if(self.maxX > 12):
            self.window.addstr(0, self.maxX-1, "x")
            self.window.addstr(0, self.maxX-3, "=")
            self.window.addstr(0, self.maxX-5, "/")
        elif(self.maxX < 12):
            self.window.addstr(0, self.maxX-1, "x")
            self.window.addstr(0, self.maxX-2, "=")
            self.window.addstr(0, self.maxX-3, "/")
        else:
            return


    def resizeAfterUnsnap(self):
        self.maxX *= .5
        self.maxY *= .5
        self.ceilCoordsNScale()
        self.window.resize(self.maxY, self.maxX)

    def snapToRightHalf(self, newY, newX, timeSinceReleased):
        #TODO: not necessary but try and add the windows half opacity before snap so you know what your getting into

        #Snaps when you let go and your mouse is over the border
        # rightHalfCenterY, rightHalfCenterX = Settings.MAX_Y / 2, (Settings.MAX_X + Settings.MAX_X/2) /2
        currTime = time.time()
        if(not self.isBeingHeld and newX >= Settings.MAX_X - 1 and currTime - timeSinceReleased <= Settings.RELEASE_SNAPBUFFER):
            newY, newX = self.validatePosition(newY,newX)
            rightHalfCenterX = (Settings.MAX_X + Settings.MAX_X/2) / 2
            self.move(1,int(rightHalfCenterX - self.maxX/2))
            self.maxY = Settings.MAX_Y - 1
            self.maxX = Settings.MAX_X /2
            self.ceilCoordsNScale()


            self.window.resize(self.maxY, self.maxX)
            self.clear()
            self.isSnapped = True



    def move(self,y,x):
        if(windowManager.isWindowHeld == self):
            self.ceilCoordsNScale()
            validPositionY, validPositionX = self.validatePosition(y,x)
            self.WindowCoordsToMouseCoords(y,x)
            self.window.mvwin(validPositionY, validPositionX)
            self.isBeingHeld = True

            if(self.isSnapped):
                self.isSnapped = False
                self.resizeAfterUnsnap()
        elif(windowManager.isWindowHeld is None):
            windowManager.isWindowHeld = self

    def resizeWindow(self, newY, newX, pressed):
        # BUG: when resizing an issue occurs that after the first resize, it seems to snap back to the orignal when you start resizing again i belive this is due to the math being applied to newX in the call of this method
        if(pressed or (self.isBeingResized and pressed)):
            newY, newX = self.checkIfMinSize(newY,newX)
            self.window.resize(newY, newX)
            self.window.refresh()
            self.isBeingResized = True
            self.finalY = newY 
            self.finalX = newX
        else:
            self.isBeingResized = False
            self.maxY = self.finalY
            self.maxX = self.finalX
            self.window.resize(self.maxY, self.maxX)

    def checkAndMove(self,my,mx,pressed):
        """Higher method than move for checking of the mouses pressed to de-clutter updateWindow"""
        if(pressed or (self.isBeingHeld and pressed)):
            self.move(my,mx)
            self.released = time.time() #time needed for snapping
        else:
            self.isBeingHeld = False
            windowManager.isWindowHeld = None
            self.timeSinceReleased = time.time() # time needed for snapping
            self.snapToRightHalf(my,mx, self.timeSinceReleased)

    def checkIfMinSize(self, sizeY, sizeX):
        if(sizeY < Settings.MIN_WINDOW_Y):
            sizeY = Settings.MIN_WINDOW_Y
        if(sizeX < Settings.MIN_WINDOW_X):
            sizeX = Settings.MIN_WINDOW_X
        return sizeY, sizeX
            

    def isTopBorder(self, my, mx, margin=0):
        if(my <= self.y + margin and my >= self.y):
            if(mx <= self.x + self.maxX and mx >= self.x):
                return True

    def isRightBorder(self, my, mx, margin=0):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + self.maxX + margin and mx >= self.x + self.maxX):
                return True
            
    def isLeftBorder(self, my, mx, margin=0):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + margin and mx >= self.x):
                return True

    def ifClickedInside(self, my,mx):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + self.maxX and mx >= self.x):
                return True
        return False