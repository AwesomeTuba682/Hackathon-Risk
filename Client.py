
import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
            self.receive_messages()
            self.send_message()
        except Exception as e:
            print(f"Error: {e}")

    def receive_messages(self):
        receive_thread = threading.Thread(target=self.receive_thread_func)
        receive_thread.start()

    def receive_thread_func(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"Received from server: {message}")
            except Exception as e:
                print(f"Error: {e}")
                break

    def send_message(self):
        while True:
            try:
                message = input("Enter message: ")
                self.client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
                break


client = Client('127.0.0.1', 5555)




