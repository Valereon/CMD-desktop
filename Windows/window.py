import curses
import math
import time

from entity import Entity
from Settings import Settings
from Windows.windowManager import windowManager


class Window(Entity):
    def __init__(self, name: str, sizeY: int, sizeX: int, resize: bool):
        #self.id = 1  # TODO: make an id system to assign unique ids  # noqa: ERA001
        self.sizeY = sizeY
        self.sizeX = sizeX

        self.isBeingHeld = False
        self.isSnapped = False
        self.resizable = resize
        self.released = 0
        self.timeSinceReleased = 0

        self.window = curses.newwin(self.sizeY, self.sizeX, 1, 1)
        self.maxY, self.maxX = self.window.getmaxyx()

        super().__init__(name, self.maxX, self.maxY)

    def updateWindow(self, my, mx, pressed) -> None:
        self.window.border("|", "|", "-", "-", "+", "+","+","+")
        self.displayWindowTitle()
        self.window.refresh()
        self.ceilCoordsNScale()


        if(self.isTopBorder(my,mx,1) or self.isBeingHeld):
            self.checkAndMove(my,mx,pressed)

        if(self.ifClickedInside(my, mx) and pressed):
            windowManager.focusWindow(self)

    def ceilCoordsNScale(self):
        """This method is essitnal thanks to my stupid math so instead of having a bunch of math.ceil in and around the scripts im just gonna set it here for cleanliness
        well if it causes issues oh well

        """
        self.x = math.ceil(self.x)
        self.y = math.ceil(self.y)
        self.maxX = math.ceil(self.maxX)
        self.maxY = math.ceil(self.maxY)

    def WindowCoordsToMouseCoords(self,my,mx):
        """This method is just making the windows coordiantes the mouse cordiantes"""
        self.y = my
        self.x = mx

    def clear(self):
        self.window.clear()

    def displayWindowTitle(self):
        self.window.addstr(0,0, self.name)
        # no clue why this dosent work
        # TODO: Fix this window minmize x and maximazie
        self.window.addstr(0, self.maxX-1, "x")
        self.window.addstr(0, self.maxX-2, "=")
        self.window.addstr(0, self.maxX-3, "/")


    def ifClickedInside(self, my,mx):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + self.maxX and mx >= self.x):
                return True
        return False

    def resizeAfterUnsnap(self):
        self.maxX *= .5
        self.maxY *= .5
        self.ceilCoordsNScale()
        self.window.resize(self.maxY, self.maxX)

    def snapToRightHalf(self, newY, newX, timeSinceReleased):
        #TODO: not nessecary but try and add the windows half opacity before snap so you know what your getting into

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

    def checkAndMove(self,my,mx,pressed):
        if(pressed or (self.isBeingHeld and pressed)):
            self.move(my,mx)
            self.released = time.time() #time needed for snapping
        else:
            self.timeSinceReleased = time.time() # time needed for snapping
            self.snapToRightHalf(my,mx, self.timeSinceReleased)


    def move(self,y,x):
        if(windowManager.isWindowHeld == self):
            self.ceilCoordsNScale()
            self.validatePosition(y,x)
            self.WindowCoordsToMouseCoords(y,x)
            self.window.mvwin(self.y, self.x)

            if(self.isSnapped):
                self.isSnapped = False
                self.resizeAfterUnsnap()
            self.isBeingHeld = True

        elif(windowManager.isWindowHeld is None):
            windowManager.isWindowHeld = self

        else:
            self.isBeingHeld = False
            windowManager.isWindowHeld = None










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
            
    def isLeftBorder(self, my, mx, margin=0):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + margin and mx >= self.x):
                return True
