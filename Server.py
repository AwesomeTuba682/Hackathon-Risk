import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.current_turn = 0
        self.start_server()

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # prevent random people / AFK people
        print(f"Server listening on {self.host}:{self.port}")
        self.accept_connections()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            self.clients.append(client_socket)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        client_id = self.clients.index(client_socket)
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Received from client {client_id}: {message}")
                self.process_message(client_id, message)
            except Exception as e:
                print(f"Error: {e}")
                break
        client_socket.close()
        self.clients.remove(client_socket)

    def process_message(self, client_id, message):
        if client_id == self.current_turn:
            if message.lower() == "end turn":
                self.switch_turn()
                self.send_client_message(client_id, "Your turn is over!")

            else:
                self.handle_logic(client_id, message)
        else:
            self.send_client_message(client_id, message)

    def handle_logic(self, client_id, message):
        print("Im gay")

    def switch_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.clients)

    def send_client_message(self, client_id, message):
        try:
            self.clients[client_id].send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")

    def broadcast_message(self, message):
        for client_socket in self.clients:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")


server = Server('0.0.0.0', 5555)




