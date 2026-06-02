import socket
import threading

# Konfigurasi Server
HOST = '0.0.0.0' 
PORT = 10005      

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, current_client):
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                remove(client)

def handle_client(client, addr):
    ip_port = f"{addr[0]}:{addr[1]}"
    print(f"[KONEKSI BARU] {ip_port} terhubung.")
    
    join_msg = f"{addr[0]}#{addr[1]}> joined\n".encode('utf-8')
    broadcast(join_msg, client)

    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                formatted_msg = f"{addr[0]}#{addr[1]}> {message}\n"
                print(f"[BROADCAST] {formatted_msg.strip()}")
                broadcast(formatted_msg.encode('utf-8'), client)
            else:
                remove(client)
                break
        except:
            remove(client)
            break

def remove(client):
    if client in clients:
        clients.remove(client)
        client.close()

print(f"[STARTING] Server berjalan di port {PORT}...")
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()