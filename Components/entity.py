import Settings.Settings as Settings


class Entity():
    """this is the base class for a lot of objects for the reason of shared methods and easy extendability"""
    def __init__(self, name, maxX, maxY) -> None:
        self.name = name
        self.x = 0
        self.y = 0
        self.maxX = maxX
        self.maxY = maxY
        #these are used to figure out the global position if the entity is in a sub window it wont report the mouse correctly
        self.globalPosX = 0
        self.globalPosY = 0
        
    
    def getGlobalCoordinates(self, win):
        y,x = win.getbegyx()
        self.globalPosX = self.x + x
        self.globalPosY = self.y + y
        
    
    def validatePosition(self, newY, newX):
        """Turns any invalid position into a valid position"""
        if newX + self.maxX > Settings.MAX_X:
            newX = Settings.MAX_X - self.maxX
        if newY + self.maxY > Settings.MAX_Y:
            newY = Settings.MAX_Y - self.maxY
        if newX < 0:
            newX = 0
        if newY < 0:
            newY = 0
        return newY, newX

    def isTopBorder(self, my, mx, margin=0):
        if(my <= self.y + margin and my >= self.y):
            if(mx <= self.x + self.maxX and mx >= self.x):
                return True
            
    def isBottomBorder(self, my, mx, margin=0):
        if my <= self.y + self.maxY + margin and my >= self.y + self.maxY:
            if mx <= self.x + self.maxX and mx >= self.x:
                return True
        return False

    def isRightBorder(self, my, mx, margin=0):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + self.maxX + margin and mx >= self.x + self.maxX):
                return True
            
    def isLeftBorder(self, my, mx, margin=0):
        if(my <= self.y + self.maxY and my >= self.y):
            if(mx <= self.x + margin and mx >= self.x):
                return True

    def isPointInside(self, my,mx, useGlobal=False):
        if(useGlobal):
            if(my <= self.globalPosY + self.maxY and my >= self.globalPosY):
                if(mx <= self.globalPosX + self.maxX and mx >= self.globalPosX):
                    return True
            return False
        else:
            if(my <= self.y + self.maxY and my >= self.y):
                if(mx <= self.x + self.maxX and mx >= self.x):
                    return True
            return False