import socket
import threading
import sys

SERVER_IP = '127.0.0.1'  
SERVER_PORT = 10005

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, SERVER_PORT))
    print("Selamat Datang di Chatroom")
except Exception as e:
    print(f"Gagal terhubung ke server: {e}")
    sys.exit()

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(message, end="")
            else:
                break
        except:
            print("\n[INFO] Terputus dari server.")
            client.close()
            break

def send_messages():
    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                client.close()
                break
            client.send(message.encode('utf-8'))
        except:
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

send_messages()