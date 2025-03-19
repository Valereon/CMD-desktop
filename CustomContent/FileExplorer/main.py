from Components.window import Window
from Settings import Settings
import os

PROGRAM_NAME = "File Explorer" # the one for visual stuff like icons
REFERENCE_NAME = "FileExplorer" # the one that will be internally used to call the program must be same as the class

# list all folders in a directory and files and display them
# be able to double click on a folder to change directories and go back
# display full path at the top


class FileExplorer(Window):
    def __init__(self):
        self.fullPath = ""
        self.currentFolder = ""        
        super().__init__(PROGRAM_NAME) 
        # self.customUpdate = self.update
    
        
    # def update(self):
        # self.move(5,5)
                
    
    def changeDirectory(self,newFolder):
        # if(self.fullPath.__contains__(newFolder))
        os.chdir(f"{self.fullPath}/{newFolder}")
        
        
    
    
    
    
    