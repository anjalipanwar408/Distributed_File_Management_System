
# delete file from the directory

import colorama as c
import os
import sys
def deleteFile(fileName):
    global currWorkingDir
    if currWorkingDir == None:
        return c.Fore.RED+"No directory is selected"+c.Fore.RESET
    if fileName not in currWorkingDir.files.keys():
        return c.Fore.RED+"File not found"+c.Fore.RESET
    # get the file
    file = currWorkingDir.files[fileName]
    for inode in file.Inodes:
        # delete the file from the disk
        del Memory[inode]
    # delete the file from the directory
    del currWorkingDir.files[fileName]
    return c.Fore.GREEN+"File deleted successfully"