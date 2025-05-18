# function to open file using filename
import colorama as c

def openFile(fileName, currWorkingDir, mode, currWorkingFile, FileOpenMode):
    global openFiles
    if fileName not in currWorkingDir.files.keys():
        return c.Fore.RED+"File not found"+c.Fore.RESET
    if currWorkingFile != None and currWorkingFile.name != fileName:
        return c.Fore.RED+"You have Another File "+currWorkingFile.name + " already opened!"+c.Fore.RESET, currWorkingFile, FileOpenMode
    if fileName in openFiles.keys() and openFiles[fileName][1] == 'w' and openFiles[fileName][0] == currWorkingDir.name:
        return c.Fore.RED+"File "+fileName + " already opened for writing! \nPlease wait for writer to close file"+c.Fore.RESET, currWorkingFile, FileOpenMode
    if fileName in openFiles.keys() and openFiles[fileName][1] == 'r' and openFiles[fileName][0] == currWorkingDir.name and mode == 'w':
        return c.Fore.RED+"File "+fileName + " already opened for reading!\n Please wait for reader to close the file"+c.Fore.RESET, currWorkingFile, FileOpenMode
    if fileName in openFiles.keys() and openFiles[fileName][1] == 'w' and openFiles[fileName][0] == currWorkingDir.name and mode == 'r':
        return c.Fore.RED+"File "+fileName + " already opened for writing!\n Please wait for writer to close the file"+c.Fore.RESET, currWorkingFile, FileOpenMode
    if fileName in openFiles.keys() and openFiles[fileName][1] == 'r' and openFiles[fileName][0] == currWorkingDir.name:
        currWorkingFile = currWorkingDir.files[fileName]
        FileOpenMode = 'r'
        return c.Fore.GREEN+"File "+fileName + " opened for reading!"+c.Fore.RESET, currWorkingFile, FileOpenMode
    if fileName in openFiles.keys() and openFiles[fileName][1] == 'w' and openFiles[fileName][0] != currWorkingDir.name:
        if mode == "":
            return c.Fore.RED+"Enter a valid mode to open the file"+c.Fore.RESET
        if currWorkingDir == None:
            return c.Fore.RED+"No directory is selected"+c.Fore.RESET
        if fileName not in currWorkingDir.files.keys():
            return c.Fore.RED+"File not found"+c.Fore.RESET
        currWorkingFile = currWorkingDir.files[fileName]
        openFiles[fileName] = [currWorkingDir.name, mode]
        return c.Fore.GREEN+"File "+currWorkingFile.name+" opened successfully for writing"+c.Fore.RESET, currWorkingFile, mode
    if fileName in openFiles.keys() and openFiles[fileName][1] == 'r' and openFiles[fileName][0] != currWorkingDir.name:
        if mode == "":
            return c.Fore.RED+"Enter a valid mode to open the file"+c.Fore.RESET
        if currWorkingDir == None:
            return c.Fore.RED+"No directory is selected"+c.Fore.RESET
        if fileName not in currWorkingDir.files.keys():
            return c.Fore.RED+"File not found"+c.Fore.RESET
        currWorkingFile = currWorkingDir.files[fileName]
        FileOpenMode = mode
        openFiles[fileName] = [currWorkingDir.name, mode]
        return c.Fore.GREEN+"File "+currWorkingFile.name+" opened successfully for reading"+c.Fore.RESET, currWorkingFile, mode
    if mode == "":
        return c.Fore.RED+"Enter a valid mode to open the file"+c.Fore.RESET
    if currWorkingDir == None:
        return c.Fore.RED+"No directory is selected"+c.Fore.RESET
    if fileName not in currWorkingDir.files.keys():
        return c.Fore.RED+"File not found"+c.Fore.RESET
    currWorkingFile = currWorkingDir.files[fileName]
    FileOpenMode = mode
    openFiles[fileName] = [currWorkingDir.name, mode]
    text = (c.Fore.GREEN+"File "+currWorkingFile.name +
            " opened successfully"+c.Fore.RESET)
    return text, currWorkingFile, FileOpenMode