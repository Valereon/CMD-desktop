class WindowManager():
    def __init__(self):
        self.isWindowHeld = False
        
        self.focusedWindow = None # the window which will take highest prioty and is in focus and ticking
        self.activeWindows = [] #windows that are not in focus but still ticking
        self.unfocusedWindows = [] # windows that are not in focus and not ticking
        self.minimizedWindows = [] # windows that are minimized and not ticking 
        
    
    def update(self, my, mx, pressed, timeSinceReleased):
        for i in self.activeWindows:
            i.updateWindow(my, mx, pressed, timeSinceReleased)
        if(self.focusedWindow is not None):
            self.focusedWindow.updateWindow(my, mx, pressed, timeSinceReleased)
    
    
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