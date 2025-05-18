def multi_threaded_client(connection):
    global root, Menu, openFiles
    connection.send(str.encode(
        'Please enter your name: '))
    name = connection.recv(2048)
    name = name.decode('utf-8')
    users.append(name)
    print(f'User {name} has connected!')
    print(users)
    currentWorkingDir = root
    currentWorkingFile = None
    OpenFileMode = None
    connection.send(str.encode(
        c.Fore.GREEN+"You have joined the Server Successfully"+c.Fore.RESET+Menu))
    while True:
        data = connection.recv(2048)
        data = data.decode('utf-8')
        response, currentWorkingDir, currentWorkingFile, OpenFileMode = execute(
            data, currentWorkingDir, currentWorkingFile, OpenFileMode)
        if not data or data == "Exit" or data == "exit":
            print(name + ' disconnected!')
            users.remove(name)
            print("\nCurrent Users in the File System: ", users)
            # dump the memory and root to pickle
            with open("data.pickle", "wb") as f:
                pickle.dump([root, Memory], f)
            break
        print(openFiles)
        connection.sendall(str.encode(
            response+Menu+c.Fore.MAGENTA+getPathOfCWD(root, currentWorkingDir.name)+c.Fore.RESET+"\n"))
    connection.close()


"""
this is the main function where the file system starts
"""

if _name_ == "_main_":

    # loading the root from pickle and the global memory
    try:
        ls = pickle.load(open("data.pickle", "rb"))
        Memory = ls[1]
        root = ls[0]
        currWorkingDir = root
    # perform file operations
    except:
        rootDir = Directory("root")
        root = rootDir
        currWorkingDir = rootDir

    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening..')
    ServerSideSocket.listen(5)

    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()