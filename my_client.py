import socket

def start_client(server_ip='127.0.0.1', server_port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        while True:
            data = s.recv(1024).decode()
            if not data:
                break
            print(data, end='')

            if data.strip().endswith(':') or data.strip().endswith('>'):
                user_input = input()
                s.sendall(user_input.encode())
            if "Closing connection" in data or "disconnected" in data:
                break

if __name__ == "__main__":
    start_client()
