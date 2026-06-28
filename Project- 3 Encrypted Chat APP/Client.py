import socket
import threading
from shared_crypto import encrypt, decrypt

SERVER_IP = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def receive():
    while True:
        try:
            msg = client.recv(4096).decode()
            if msg:
                print("\n[Encrypted Broadcast]:", msg)
                print("[Decrypted]:", decrypt(msg))
        except:
            print("Connection closed")
            break

def send():
    while True:
        try:
            msg = input("You: ")
            encrypted = encrypt(msg)
            client.send(encrypted.encode())
        except:
            print("Send error")
            break

threading.Thread(target=receive, daemon=True).start()
threading.Thread(target=send, daemon=True).start()

while True:
    pass