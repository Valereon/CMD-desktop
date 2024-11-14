import curses
import Settings


class Window:
    def __init__(self, name: str, sizeY: int, sizeX: int, resize: bool, border: list):
        self.name = name
        self.id = 1  # TODO: make an id system to assign unique ids
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.x = 0
        self.y = 0
        self.resizable = resize
        self.border = []
        self.maxX = 0
        self.maxY = 0
        self.setup()

    def setup(self):
        self.window = curses.newwin(self.sizeY, self.sizeX, 1, 1)
        self.maxY, self.maxX = self.window.getmaxyx()

    def tick(self):
        self.window.border("|", "|", "-", "-", "+", "+", "+", "+")
        self.window.refresh()

    def clear(self):
        self.window.clear()

    def move(self, newY, newX):
        result = self.checkIfLegal(newY, newX)
        if(result == -1):
            newX = self.x
        elif(result == -2):
            newY = self.y

        self.window.mvwin(newY, newX)
        self.x = newX
        self.y = newY

    def checkIfLegal(self, y, x):
        if self.maxX + x >= Settings.MAX_X:
            return -1
        if self.maxY + y >= Settings.MAX_Y:
            return -2
        
    def snapToHalf():
        pass