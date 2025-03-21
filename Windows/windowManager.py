from Data import GlobalVars as GV


class WindowManager:
    def __init__(self):
        self.isWindowHeld = False

        self.focusedWindow = None  # the window which will take highest prioty and is in focus and ticking
        self.activeWindows = []  #windows that are not in focus but still ticking
        self.unfocusedWindows = [] # windows that are not in focus and not ticking
        self.minimizedWindows = [] # windows that are minimized and not ticking


    def update(self):
        for i in self.activeWindows:    
            i.internalUpdate(GV.mouseY, GV.mouseX, GV.isMouse0Pressed)
        if(self.focusedWindow is not None):
            self.focusedWindow.internalUpdate(GV.mouseY, GV.mouseX, GV.isMouse0Pressed)


    def focusWindow(self, window):
        self.focusedWindow = window


    def addWindow(self, window):
        self.activeWindows.append(window)

    def removeWindow(self, window):
        if(self.unfocusedWindows.__contains__(window)):
            self.unfocusedWindows.remove(window)
        if(self.activeWindows.__contains__(window)):
            self.activeWindows.remove(window)
        if(self.minimizedWindows.__contains__(window)):
            self.minimizedWindows.remove(window)


    def minimize():
        pass
    def unMinimize():
        pass




windowManager = WindowManager()
