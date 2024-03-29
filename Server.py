import socket
import threading
from Board import *
from Player import *

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.players = []
        self.current_turn = 0
        self.first_turn = True
        self.board = Board(5,5)
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
            player = Player(len(self.clients)-1, 10)
            self.players.append(player)
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
            self.send_client_message(client_id, self.handle_logic(client_id, message))
            print(self.board)

        else:
            self.send_client_message(client_id, "Not your turn")

    def handle_logic(self, client_id, message):
        player = self.players[client_id]
        split_msg = message.split()
        try:
            split_msg[1:] = list(map(int, split_msg[1:]))

        except:

            return "Check function inputs"

        match split_msg[0].lower():

            case "place":
                if len(split_msg) != 4: # check ints
                    return "Check function inputs"

                tile = self.board.get(split_msg[1], split_msg[2])
                msg = self.board.place(player, tile, split_msg[3])
                if msg != True:
                    return msg

                if self.first_turn:
                    self.switch_turn()
                    self.send_client_message(client_id, "Your turn is over!")

                return "place complete"

            case "move":
                if len(split_msg) != 6: # check ints
                    return "Check function inputs"

                from_tile = self.board.get(split_msg[1], split_msg[2])
                to_tile = self.board.get(split_msg[3], split_msg[4])
                msg = self.board.move(player, from_tile, to_tile, split_msg[5])
                if msg != True:
                    return msg

                self.switch_turn()
                self.send_client_message(client_id, "Your turn is over!")
                return "move complete"

            case "capture":
                if len(split_msg) != 6: # check ints
                    return "Check function inputs"

                attacking_tile = self.board.get(split_msg[1], split_msg[2])
                defending_tile = self.board.get(split_msg[3], split_msg[4])
                msg = self.board.capture(player, attacking_tile, defending_tile, split_msg[5])
                if msg != True:
                    return msg

                return "capture complete"

            case "end":
                self.switch_turn()
                self.send_client_message(client_id, "Your turn is over!")

        return "Function not found"



    def switch_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.clients)
        if self.current_turn == 0:
            self.first_turn = False
            for player in self.players:
                player.available_troops = 0

            for i in range(self.board.n):
                for j in range(self.board.m):
                    tile_worth = 1
                    owner_id = self.board.get(i, j).owner
                    self.players[owner_id].available_troops += tile_worth



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

def check_for_ints(arr):
    for number in arr:
        if not isinstance(number, int):
            return False
    return True


server = Server('0.0.0.0', 5555)




