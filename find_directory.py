def findDirectory(dir, dirName):
    if (dir.name == dirName):
        return dir
    else:
        for directory in dir.subdirectories.keys():
            foundDir = findDirectory(dir.subdirectories[directory], dirName)
            if (foundDir != None):
                return foundDir
        return None