import socket
import threading
from time import sleep
from dataclasses import dataclass
from typing import List
from process_request_server import Message

@dataclass
class Player:
    client: object
    addr: str
    name: str = None
    playing: bool = False
    score:int = 0

server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 8080
client_name = " "
clients = []
players: List[Player] = []
clients_names = []
player_data = []



close_server = False
# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT # code is fine without this


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print (socket.AF_INET)
    print (socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    # threading._start_new_thread(accept_clients, (server, " "))



# Stop server function
def stop_server():
    global server
    server.close()



def accept_clients(the_server, y):
    global close_server
    while True:
        try:
            client, addr = the_server.accept()
            print("New client accepted")
            clients.append(client)
            new_player = Player(client=client,addr=addr)
            players.append(new_player)
            print('new player added')
            # use a thread so as not to clog the gui thread
            threading._start_new_thread(send_receive_client_message, (client, addr))
        except Exception as e:
            print (e)
            close_server = True
            break
start = False
# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data, player0, player1, start


    while True:
        try:
            message = Message(client_connection,(HOST_ADDR, HOST_PORT))
            print(message)
        except Exception as e:
            print(e)

        try:
            message.process_events('r')
        except Exception as e:
            print(
                "main: error: exception for",
                f"{message.addr}"
            )
            print(e)

        # print('listen to client')
        # if start:
        #     sleep(2)
        #     client_connection.send("Start the game".encode())
        #     start = False
        # else:
        #
        #     data = client_connection.recv(4096)
        #     if not data: break
        #     print(data)
        #     if data == b'magic':
        #         start = True
        #     else:
        #         client_connection.send("welcome1".encode())

# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects
start_server()

server.settimeout(60)

while True:
    if close_server:
        server.close()
        break
    threading._start_new_thread(accept_clients, (server, " "))
print('done')