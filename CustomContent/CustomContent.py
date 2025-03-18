import os
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
        if(dirs[i] == "CustomContent.py"):
            continue
        customApps.append(dirs[i])
    return customApps


def registerApps():
    pass



def main():
    customApps = getCustomApps()
    