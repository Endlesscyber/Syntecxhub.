import socket
import threading
from shared_crypto import decrypt
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

clients = []

def log_message(msg):
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {msg}\n")

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    clients.append(conn)

    while True:
        try:
            data = conn.recv(4096).decode()
            if not data:
                break

            decrypted = decrypt(data)

            log_message(f"{addr}: {decrypted}")
            print(f"{addr} -> {decrypted}")

            broadcast(data, conn)

        except:
            break

    clients.remove(conn)
    conn.close()
    print(f"[DISCONNECTED] {addr}")

# ---------- MAIN SERVER ----------
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[SERVER STARTED] {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()