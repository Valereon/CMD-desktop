import Settings.Settings as Settings


class Entity():
    def __init__(self, name, maxX, maxY) -> None:
        self.name = name
        self.x = 0
        self.y = 0
        self.maxX = maxX
        self.maxY = maxY
        
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