
# class to represent a directory

import colorama as c

class Directory:

    # Constructor
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

    # Add file to directory
    def addFile(self, file):
        if (file.name in self.files.keys()):
            return c.Fore.RED+"File already exists"+c.Fore.RESET
        else:
            self.files[file.name] = file
            return c.Fore.GREEN+"File created successfully"+c.Fore.RESET

    # Add subdirectory to directory

    def addSubdirectory(self, directory):
        if (directory.name in self.subdirectories.keys()):
            return c.Fore.RED+"Directory already exists" + c.Fore.RESET

        else:
            self.subdirectories[directory.name] = directory
            return (c.Fore.GREEN+"Directory created successfully"+c.Fore.RESET)
