def moveWithinFile(s, t, currWorkingFile):
    if (currWorkingFile == None):
        return c.Fore.RED+"No file is opened"+c.Fore.RESET
    if (s > len(currWorkingFile.Inodes) or t > len(currWorkingFile.Inodes) or s < 1 or t < 1):
        return "Line number out of range"
    if (s == t):
        return c.Fore.RED+"Source and destination are same"+c.Fore.RESET
    # pop the line from source
    inode = currWorkingFile.Inodes[s-1]
    # store line at destination
    currWorkingFile.Inodes[t-1] = inode
    currWorkingFile.Inodes.pop(s-1)
    # updating the size of file
    currWorkingFile.size = 0
    for index in currWorkingFile.Inodes:
        currWorkingFile.size += len(Memory[index])
    return c.Fore.GREEN+"Text moved successfully"+c.Fore.RESET