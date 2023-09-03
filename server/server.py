import socket
import threading


def handle_request(client_request):
    pass


def main():
    host = '127.0.0.1'
    port = 15000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)

    print(f"Server listening on {host}:{port}")

    while True:
        client_request, _ = server_socket.accept()

        client_thread = threading.Thread(target=handle_request, args=(client_request,))
        client_thread.start()


if __name__ == "__main__":
    main()
