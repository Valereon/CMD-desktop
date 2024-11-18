import curses
import Settings
import time

class Window:
    def __init__(self, name: str, sizeY: int, sizeX: int, resize: bool):
        self.name = name
        self.id = 1  # TODO: make an id system to assign unique ids
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.x = 0
        self.y = 0
        self.maxY = 0
        self.maxX = 0
        self.isBeingHeld = False
        # self.isSnapped = False
        self.resizable = resize
        self.snapTime = 0.5
        self.setup()

    def setup(self):
        self.window = curses.newwin(self.sizeY, self.sizeX, 1, 1)
        self.maxY, self.maxX = self.window.getmaxyx()

    def tick(self):
        self.window.border("|", "|", "-", "-", "+", "+","+","+")
        self.window.refresh()

    def clear(self):
        self.window.clear()

    def move(self, newY, newX):
        newY, newX = self.checkIfLegal(newY,newX)
        self.window.mvwin(newY, newX)
        self.x = newX
        self.y = newY

    #TODO: Implement custom border for the windows
    def border():
        pass
        



    def checkIfLegal(self, newY, newX):
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
        
    def snapToHalf(self, newY, newX):
        #TODO: make it so when you unsnap the window it gets smaller like on windows
        #TODO: not nessecary but try and add the windows half opacity before snap so you know what your getting into
        #Snaps when you let go and your mouse is over the border
        if(not self.isBeingHeld and newX >= Settings.MAX_X - 1):
            newY, newX = self.checkIfLegal(newY,newX)
            # rightHalfCenterY, rightHalfCenterX = Settings.MAX_Y / 2, (Settings.MAX_X + Settings.MAX_X/2) /2
            rightHalfCenterX = (Settings.MAX_X + Settings.MAX_X/2) /2
            self.move(0, int(rightHalfCenterX - self.maxX/2))

            self.maxY = int(Settings.MAX_Y - 2)
            self.maxX = int(Settings.MAX_X /2)


            self.window.resize(self.maxY, self.maxX)
            self.clear()

            

            
        