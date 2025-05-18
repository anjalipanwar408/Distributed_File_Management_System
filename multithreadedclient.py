def execute(line, currWorkingDir, currWorkingFile, FileOpenMode):
    global root, Memory, MEMORYMAP
    res = ""
    line = line.lower()
    # iterate over the lines
    line = line.split()
    if "write_to_file" in line and "write_at" in line:
        data = line[3:]
        # join data without spaces
        data = " ".join(data)
        lineNo = int(line[2])
        res = "Write to file (lineNo,data): "+str(lineNo)+" --> "
        res += writeToFile("write_at", currWorkingFile,
                           FileOpenMode, data, lineNo)
    elif "write_to_file" in line:
        data = line[2:]
        data = " ".join(data)
        res = "Write to file (data): --> "
        res += writeToFile("append", currWorkingFile, FileOpenMode, data, None)
    elif len(line) == 2:
        command, arg = line
        if command == "create_file":
            res = createFile(arg, currWorkingDir)
        elif command == "delete_file":
            res = deleteFile(arg)
        elif command == "make_directory":
            res = createDirectory(arg, currWorkingDir)
        elif command == "change_directory":
            resDir = findDirectory(root, arg)
            if resDir == None:
                res = c.Fore.RED+"Directory not found\n"+c.Fore.RESET
            else:
                currWorkingDir = resDir
                res = c.Fore.GREEN+"The directory has been changed to: " + arg+"\n"+c.Fore.RESET
        elif command == "truncate_file":
            res = truncateFile(int(arg), currWorkingFile)
        elif command == "read_from_file":
            res = c.Fore.GREEN+"Read from file Sequentially --> \n"+c. Fore.RESET
            res += readFromFile(True, currWorkingFile,
                                FileOpenMode, None, None)
        else:
            res = c.Fore.RED+"Invalid command\n"+c.Fore.RESET
    elif len(line) == 1:
        command = line[0]
        if command == "close_file":
            res, currWorkingFile, FileOpenMode = closeFile(currWorkingFile)
        elif command == "show_memory_map":
            res = "Memory Map:\n"
            printTree(root, 0, currWorkingDir)
            if MEMORYMAP != "":
                res = MEMORYMAP+"\n"
                MEMORYMAP = ""
        elif command == "go_to_root":
            currWorkingDir = root
            res = c.Fore.GREEN+"The directory has been changed to: root\n"+c.Fore.RESET
        else:
            res = c.Fore.RED+"Invalid command\n" + c.Fore.RESET
    elif len(line) == 3:
        command, arg1, arg2 = line
        if command == "move_file":
            res = moveFile(arg1, arg2)
        elif command == "read_from":
            res = "Read from file (start,size): "+arg1+" "+arg2+" --> "
            res += readFromFile(False, currWorkingFile,
                                FileOpenMode, int(arg1), int(arg2))
        elif command == "move_within_file":
            res = "Move within file (source,target): " + \
                arg1+" "+arg2+" --> "
            res += moveWithinFile(int(arg1), int(arg2), currWorkingFile)
        elif command == "open_file":
            if arg1 not in currWorkingDir.files.keys():
                res = c.Fore.RED+"File not found\n" + c.Fore.RESET
                return res, currWorkingDir, currWorkingFile, FileOpenMode
            # call open file function
            res, currWorkingFile, FileOpenMode = openFile(
                arg1, currWorkingDir, arg2, currWorkingFile, FileOpenMode)
        else:
            res = c.Fore.RED+"Invalid command\n" + c.Fore.RESET
    else:
        res = c.Fore.RED+"Invalid command\n" + c.Fore.RESET
    return res, currWorkingDir, currWorkingFile, FileOpenMode