import socket
import threading
import json
import tkinter as tk
from Board import Board

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_id = -999
        self.map = Board()
        self.updated_tiles = []
        self.board = [[]]
        self.actions_done = 0
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui_setup()
        self.connect_to_server()

    def gui_setup(self):

        self.highlighted_cell = None
        self.root = tk.Tk()
        self.root.title("Client")

        self.canvas = tk.Canvas(self.root, width=self.map.m*20, height=self.map.n*20, bg='black', highlightthickness=0)
        self.canvas.pack()

        self.message_text = tk.Text(self.root, height=10, width=50)
        self.message_text.pack()

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
            self.receive_messages()
            self.root.mainloop()
        except Exception as e:
            print(f"Error: {e}")

    def receive_messages(self):
        receive_thread = threading.Thread(target=self.receive_thread_func)
        receive_thread.start()

    def receive_thread_func(self):
        while True:
            try:
                message = self.client_socket.recv(32768*4).decode('utf-8')

                parts = message.split()
                if parts[0] == "your_id_is":
                    self.client_id = int(parts[1])
                    matrix_json = "".join(parts[2:])

                    self.updated_tiles = json.loads(matrix_json)
                    print(self.updated_tiles)
                    self.receive_messages()
                    self.update_gui_with_board()
                    break
                elif parts[0] == "matrix_json":
                    matrix_json = "".join(parts[1:])
                    self.updated_tiles = json.loads(matrix_json)
                    self.receive_messages()
                    self.update_gui_with_board()
                    break

                elif not message:
                    break
                print(f"Received from server: {message}")
                self.message_text.insert(tk.END, f"{message}\n")

            except Exception as e:
                print(f"Error: {e}")
                break

    def update_tiles(self):
        for i in range(17):
            self.map.tiles[i].owner = self.updated_tiles["tiles"][i]["owner"]
            self.map.tiles[i].power = self.updated_tiles["tiles"][i]["power"]
    def update_gui_with_board(self):
        self.update_tiles()
        self.canvas.delete("all")  # Clear the canvas
        colors = ["white", "gray", "red", "green", "blue", "yellow", "orange"]  # rudimentary colors

        for i, row in enumerate(self.map.board):
            for j, cell in enumerate(row):
                x1, y1 = j * 20, i * 20
                x2, y2 = x1 + 20, y1 + 20

                owner = cell.owner

                # Determine fill color based on owner
                if owner >= -2 and owner <= 5:
                    fill_color = colors[owner + 2]  # Adjusting the index to match colors list
                else:
                    fill_color = "white"  # Default to white for invalid values

                # Draw rectangle with fill color and outline
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black", tags=f"cell_{i}_{j}")

                # Bind click event to each cell
                self.canvas.tag_bind(f"cell_{i}_{j}", "<Button-1>",
                                     lambda event, row=i, col=j: self.on_cell_click(row, col))

    def on_cell_click(self, row, col):
        # print(f'{row} {col}')
        cell_value = self.map.board[row][col].owner
        # print(cell_value)
        if self.highlighted_cell is not None:
            # Perform action with coordinates of highlighted cell and clicked cell
            print(f"Highlighted cell: {self.highlighted_cell}, Clicked cell: ({row}, {col})")
            self.handle_action(self.highlighted_cell, (row,col))
        else:
            if self.actions_done == 0:
                if cell_value == -1:
                    self.handle_action((row, col), (row, col))

            if cell_value == self.client_id:
                self.highlighted_cell = (row, col)
                self.highlight_cell(row, col)

    def handle_action(self, highlighted_tile, action_tile):
        self.actions_done += 1
        action = ""
        if highlighted_tile == action_tile:
            action = f"place {action_tile[0]} {action_tile[1]} {self.get_popup_input()}"

        elif self.map.board[action_tile[0]][action_tile[1]].owner == self.client_id:
            action = f"move {highlighted_tile[0]} {highlighted_tile[1]} {action_tile[0]} {action_tile[1]} {self.get_popup_input()}"

        else:
            action = f"capture {highlighted_tile[0]} {highlighted_tile[1]} {action_tile[0]} {action_tile[1]} {self.get_popup_input()}"

        self.unhighlight_cell(highlighted_tile[0], highlighted_tile[1])
        self.send_message(action)

    def get_popup_input(self):
        popup = tk.Toplevel(self.root)
        popup.title("Enter value")

        entry = tk.Entry(popup)
        entry.pack()

        def ok_button_clicked():
            self.popup_value = entry.get()
            popup.destroy()

        ok_button = tk.Button(popup, text="OK", command=ok_button_clicked)
        ok_button.pack()

        popup.wait_window()
        return self.popup_value

    def highlight_cell(self, row, col):
        self.canvas.itemconfig(f"cell_{row}_{col}", fill="yellow")

    def unhighlight_cell(self, row, col):
        self.highlighted_cell = None
        cell_value = self.map.board[row][col].owner
        colors = ["white", "gray", "red", "green", "blue", "yellow", "orange"]  # rudimentary colors
        if cell_value >= -2 and cell_value <= 5:
            fill_color = colors[cell_value + 2]  # Adjusting the index to match colors list
        else:
            fill_color = "white"  # Default to white for invalid values
        self.canvas.itemconfig(f"cell_{row}_{col}", fill=fill_color)

    def send_message(self, message):
        try:
            self.client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")

client = Client('127.0.0.1', 5555)
