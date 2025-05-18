def readFromFile(mode, currWorkingFile, FileOpenMode, start=None, size=None):
    data = ""
    if FileOpenMode == "w":
        return c.Fore.RED+"The file is open in write-only mode"+c.Fore.RESET
    if mode == True:
        if currWorkingFile == None:
            return c.Fore.RED+"No file is opened"+c.Fore.RESET
        # read file sequentially
        for i in range(0, len(currWorkingFile.Inodes)):
            address = currWorkingFile.Inodes[i]
            data += str(i+1) + "-> " + "".join(Memory[address]) + "\n"
        return data
    else:
        return readFrom(start, size, currWorkingFile, FileOpenMode)