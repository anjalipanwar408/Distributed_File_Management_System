import socket
import threading

users = {
    "user1": "pass1",
    "user2": "pass2"
}

connected_clients = {}

def authenticate(conn):
    """
    Simple authentication protocol:
    Server asks for username and password.
    """
    conn.sendall("Username: ".encode())
    username = conn.recv(1024).decode().strip()

    conn.sendall("Password: ".encode())
    password = conn.recv(1024).decode().strip()

    if username in users and users[username] == password:
        conn.sendall(f"Authentication successful. Welcome {username}!\n".encode())
        return username
    else:
        conn.sendall("Authentication failed. Closing connection.\n".encode())
        conn.close()
        return None

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    username = authenticate(conn)
    if not username:
        print(f"[AUTH FAILED] {addr} disconnected due to failed auth.")
        return

    connected_clients[conn] = username
    try:
        while True:
            conn.sendall(f"{username}@DFS> ".encode())
            cmd = conn.recv(1024).decode().strip()
            if not cmd or cmd.lower() == 'exit':
                break
            response = f"Command received: {cmd}\n"
            conn.sendall(response.encode())
    except Exception as e:
        print(f"[ERROR] Connection with {username} lost: {e}")
    finally:
        print(f"[DISCONNECTED] {username} disconnected.")
        connected_clients.pop(conn, None)
        conn.close()

def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
