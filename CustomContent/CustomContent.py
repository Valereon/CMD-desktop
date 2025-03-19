import os
import importlib
from Data.Apps import REGISTERED_APPS #BUG TODO:this module is fucked and wont import but otherwise it works
PROJECT_ROOT = "/home/max/Projects/CMD-desktop/"
# so register the main.py to be updated when opened as a program
# do setup.py before main.py 

# loop over all the folders and run setup.py and then register main.py as a program that can be run inside of CMD-DSKTP
# setup the icon to be used as its icon
def getCustomApps():
    os.chdir(PROJECT_ROOT)
    dirs = os.listdir("CustomContent")
    customApps = []
    for i in range(len(dirs)):
        if(dirs[i] == "CustomContent.py" or dirs[i] == "__pycache__"):
            continue
        customApps.append(dirs[i])
    
    if(len(customApps) == 0):    
        raise Exception("There is no custom content in the CustomContent folder")
    
    return customApps


def registerApps(customApps):
    for i in range(len(customApps)):
        className = None
        try:
            os.chdir(f"{PROJECT_ROOT}/CustomContent/{customApps[i]}")
            module = importlib.import_module(f"CustomContent.{customApps[i]}.main")
            className = module.REFERENCE_NAME
            classReference = getattr(module, className)
        except AttributeError:
            if(className is None):
                raise Exception(f"{customApps[i]} Does not have a REFERENCE_NAME variable to denote its class name")
            else:
                raise Exception(f"{customApps[i]}s Class name is not the same as REFERENCE_NAME or class does not exist")
        REGISTERED_APPS.append(classReference)




def main():
    customApps = getCustomApps()
    registerApps(customApps)
    
    
    
main()