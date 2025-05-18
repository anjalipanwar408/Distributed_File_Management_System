# function to close opened file

import colorama as c
def closeFile(currWorkingFile):
    global openFiles
    if currWorkingFile == None:
        return c.Fore.RED+"No file is opened"+c.Fore.RESET
    if currWorkingFile.name in openFiles.keys():
        del openFiles[currWorkingFile.name]
    name = currWorkingFile.name
    currWorkingFile = None
    mode = ""
    return c.Fore.GREEN+"File " + name + " closed successfully"+c.Fore.RESET, currWorkingFile, mode