# function to create directory
import colorama as c
def createDirectory(dirName, currWorkingDir):
    global root
    if (findDirectory(root, dirName) != None):
        return c.Fore.RED+"Directory with this name already exists"+c.Fore.RESET

    if (dirName == currWorkingDir.name):
        return c.Fore.RED+"Directory with this name already exists"+c.Fore.RESET
    if (dirName == None or dirName == ""):

        return c.Fore.RED+"Directory name can not be empty"+c.Fore.RESET
    if (currWorkingDir == None):

        return c.Fore.RED+"No directory is selected"+c.Fore.RESET
    directory = Directory(dirName)
    return currWorkingDir.addSubdirectory(directory)