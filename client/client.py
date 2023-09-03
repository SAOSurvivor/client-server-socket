import socket
import struct
import time

from log_message_pb2 import LogMessage
import concurrent.futures


def send_log_message(log_level, logger, mac, message=""):
    log_message = LogMessage()
    log_message.log_level = log_level
    log_message.logger = logger
    log_message.mac = mac
    if message:
        log_message.message = message

    payload = log_message.SerializeToString()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('0.0.0.0', 15000))

        sock.sendall(struct.pack('>L', len(payload)) + payload)


def send_concurrent_messages(number_of_messages):
    messages = [
        ('DEBUG', 'dev', bytes([0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]), 'test test')
    ] * number_of_messages

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda args: send_log_message(*args), messages)


if __name__ == "__main__":
    num_messages = 100  # Number of concurrent messages to send

    send_concurrent_messages(num_messages)
