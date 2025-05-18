# function to create a file

import colorama as c
def createFile(fName, currWorkingDir):
    if (fName == None or fName == ""):
        return c.Fore.RED+"File name can not be empty"+c.Fore.RESET
    if (currWorkingDir == None):
        return c.Fore.RED+"No directory is selected"+c.Fore.RESET
    file = File(fName)
    return currWorkingDir.addFile(file)