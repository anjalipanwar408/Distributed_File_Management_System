def truncateFile(size, currWorkingFile):
    if (currWorkingFile == None):
        return c.Fore.RED+"No file is opened"+c.Fore.RESET
    if (size > currWorkingFile.size or size < 0):
        return c.Fore.RED+"Invalid size"+c.Fore.RESET

    if (size == 0):
        for index in currWorkingFile.Inodes:
            Memory[index] = None
        currWorkingFile.Inodes = []
        currWorkingFile.size = 0
        return c.Fore.GREEN+"File " + currWorkingFile.name+" truncated successfully"+c.Fore.RESET
    else:
        # calculate block numbers to be truncated
        blockNo = size//BLOCKSIZE
        if size % BLOCKSIZE != 0:
            blockNo += 1
        # truncate blocks
        for i in range(blockNo, len(currWorkingFile.Inodes)):
            Memory[currWorkingFile.Inodes[i]] = None
        currWorkingFile.Inodes = currWorkingFile.Inodes[:blockNo]
        # truncate characters
        data = Memory[currWorkingFile.Inodes[blockNo-1]]
        # subtract size from blocksize
        s = (size % BLOCKSIZE)
        Memory[currWorkingFile.Inodes[blockNo-1]] = data[:s]
        # update size of file
        currWorkingFile.size = 0
        for index in currWorkingFile.Inodes:
            currWorkingFile.size += len(Memory[index])
        return c.Fore.GREEN+"File " + currWorkingFile.name+" truncated successfully"+c.Fore.RESET