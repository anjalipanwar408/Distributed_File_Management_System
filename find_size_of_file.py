def findSizeOfFiles(root):
    global Memory
    if (root == None):
        return 0
    size = 0
    for i in root.files.keys():
        for index in root.files[i].Inodes:
            size += len(Memory[index])
    for i in root.subdirectories.keys():
        size += findSizeOfFiles(root.subdirectories[i])
    return size