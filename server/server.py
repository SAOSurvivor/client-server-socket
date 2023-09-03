import socket
import struct
import threading

from log_message_pb2 import LogMessage


def handle_request(client_socket):
    while True:
        length_prefix = client_socket.recv(4)
        if not length_prefix:
            break

        message_length = struct.unpack('>L', length_prefix)[0]

        message_data = client_socket.recv(message_length)

        if len(message_data) != message_length:
            break

        log_message = LogMessage()
        log_message.ParseFromString(message_data)

        print(f"Log Level: {log_message.log_level}")
        print(f"Logger: {log_message.logger}")
        print(f"MAC Address: {log_message.mac.hex()}")
        if log_message.message:
            print(f"Message: {log_message.message}")

    client_socket.close()


def main():
    host = '0.0.0.0'
    port = 15000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(100)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, _ = server_socket.accept()

        client_thread = threading.Thread(target=handle_request, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    main()
