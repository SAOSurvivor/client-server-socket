import socket
import struct
import threading

from log_message_pb2 import LogMessage


def handle_request(client_request):
    while True:
        length_prefix = client_request.recv(4)
        if not length_prefix:
            break

        message_length = struct.unpack('>L', length_prefix)[0]

        message_data = client_request.recv(message_length)

        if len(message_data) != message_length:
            break

        log_message = LogMessage()
        log_message.ParseFromString(message_data)

        print(f"Log Level: {log_message.log_level}")
        print(f"Logger: {log_message.logger}")
        print(f"MAC Address: {log_message.mac.hex()}")
        if log_message.message:
            print(f"Message: {log_message.message}")

    client_request.close()


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
