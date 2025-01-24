import socket

def start_server(host='0.0.0.0', port=12222):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established from {addr}")
        client_socket.sendall(b'Hello, client!')
        client_socket.close()

if __name__ == "__main__":
    start_server()
