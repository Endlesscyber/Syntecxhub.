# 🔐 Encrypted Multi-Client Chat Application (AES + TCP)

A secure real-time chat application built using **Python sockets, AES encryption, and multi-threading**.  
This project demonstrates how encrypted communication works in client-server architecture.

---

## 🚀 Features

- 🔒 AES-256 encryption for messages
- 🌐 TCP socket-based communication
- 👥 Multi-client support (concurrent connections)
- 🔁 Real-time message broadcasting
- 🧵 Multi-threaded server handling
- 📝 Server-side message logging
- 🔑 Random IV generation for each message

---

## 🧠 Tech Stack

- Python 3
- Socket Programming (TCP)
- Cryptography library (AES-CBC encryption)
- Threading

---

## 📁 Project Structure
EncryptedChatApp/
│
├── server.py
├── client.py
├── shared_crypto.py
└── chat_log.txt


---

## ⚙️ Installation

### 1️⃣ Install Python
Download Python:
https://www.python.org/downloads/

✔ Add Python to PATH

---

### 2️⃣ Install required library

```bash
pip install cryptography

How to Run
Step 1: Start Server
python server.py
Step 2: Start Client(s)

Open multiple terminals:

python client.py
💬 Working Flow
Client sends message
Message is encrypted using AES
Encrypted data sent via TCP
Server decrypts message
Message broadcast to all clients
Logs saved in chat_log.txt
🔐 Security Implementation
AES-256 encryption
CBC mode encryption
Random IV per message
PKCS7 padding
Base64 encoding
Pre-shared secret key
📸 Example Output
Client
You: hello
[Encrypted]: XyZ123....
[Decrypted]: hello
Server
[CONNECTED] ('127.0.0.1', 50210)
('127.0.0.1', 50210) -> hello

