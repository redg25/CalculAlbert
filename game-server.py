import socket
import threading
from dataclasses import dataclass
from typing import List
from process_request_client import Message
from OperationScript.operalbert import Calcul
from time import sleep
from datetime import datetime


@dataclass
class Player:
    client: object
    addr: str
    name: str = ''
    playing: bool = False
    score:int = 0
    turn: int = 1
    time_to_finish = None

server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 8080
client_name = " "
clients = []
players: List[Player] = []
# clients_names = []
# player_data = []
operations: List[tuple] = []
game_started: bool = False
game_turn: int = 1
max_turn: int = 4
game_start_time = None


def create_request(action, value):
    return dict(
        type="text/json",
        encoding="utf-8",
        content=dict(action=action, value=value),
    )


def send_new_request(client,action,value):
    request = create_request(action,value)
    message = Message(client,(HOST_ADDR,HOST_PORT))
    message.request = request
    message.process_events('w')


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection
    print('Connected to server\n'
          'Listening to clients...')
    return server


def accept_clients(the_server, y):
    while True:
        try:
            client, addr = the_server.accept()
            print("New client accepted")
            clients.append(client)
            new_player = Player(client=client,addr=addr)
            players.append(new_player)
            print('new player added')
            # use a thread so as not to clog the gui thread
            threading._start_new_thread(send_receive_client_message, (client,addr))
        except Exception as e:
            print (e)
            break




def send_receive_client_message(client_connection,addr):
    global game_started, game_turn,players, game_start_time
    global operations
    while True:
        try:
            current_player = get_player_from_client(client_connection)
            # Start the game if all the players are connected
            if are_players_ready():
                print(f'Players are ready to play...')
                game_started = True
                # Send request with countdown to clients before the game starts
                for player in players:
                    send_new_request(player.client,'wait','3')
                sleep(3)
                # Get a new operation and send it to the clients
                value = get_an_operation()
                for player in players:
                    send_new_request(player.client,'operation',value)
                    print (f'New operation sent to {player.name}')
                game_start_time = datetime.now()
                game_turn += 1
            else:
                message = Message(client_connection,(HOST_ADDR, HOST_PORT))
                message.process_events('r')
                action = message.response['action']
                value = message.response['value']
                if action == 'name':
                    current_player.name = value
                    print(f"{message.addr} sent a player name: {value}")
                    request_value = dict(nb_of_players=str(len(players)))
                    send_new_request(client_connection,'welcome',request_value)
                elif action == 'answer':
                    print(f'Received answer from {current_player.name} for it turn {current_player.turn}')
                    current_player.score += value['score']
                    current_player.turn +=1
                    # When a player finished
                    if current_player.turn == max_turn:
                        get_player_time(current_player)
                    # When a player finished but not all the other one(s)
                    if current_player.turn == max_turn and not have_players_finished(players):
                        value = dict(score=current_player.score,message="Please wait for your opponent to finish")
                        send_new_request(client_connection,'end_game',value)
                    elif have_players_finished(players):
                        # Collect all players results in a dictionary and send them to the clients
                        ls_of_results = {}
                        for player in players:
                            ls_of_results[player.name]=[player.score,player.time_to_finish]
                        value = dict(scores=ls_of_results)
                        for player in players:
                            send_new_request(player.client,'final',value)
                    # When the player is the first ready for a new operation, generate and send a new operation
                    elif len(operations)<current_player.turn:
                        print(f'{current_player.name} is the first player to play for the question {current_player.turn}')
                        value = get_an_operation()
                        send_new_request(client_connection,'operation',value)
                        game_turn += 1
                    # When the player is at least the second one ready for a new operation, send the same
                    # operation that has been sent to the first player
                    else:
                        print(f'{current_player.name} is the second player to play for the question {current_player.turn}')
                        # Get the operation to send
                        operation = operations[current_player.turn -1]
                        value = {'op_str':operation[0],'res':operation[1]}
                        send_new_request(client_connection,'operation',value)
                    print(f'{current_player.name} score is {current_player.score}')

        except Exception as e:
            print(e)
            break
    client_connection.close()


def are_players_ready() -> bool:
    all_players_have_names = True
    for player in players:
        if player.name == '':
            all_players_have_names = False
            break
    return (game_turn == 1) and len(players) == 2 and all_players_have_names



def get_player_from_client(client: socket) -> Player:
    player = [x for x in players if x.client == client][0]
    return player


# Generate a new operation
def get_an_operation() -> dict:
    c = Calcul(50,3,['+','*'],[10])
    new_op_str,res = c.make_operation()
    operations.append((new_op_str,res))
    value = {'op_str':new_op_str,'res':res}
    return value


# Set the finishing time for a player
def get_player_time(player:Player):
    end_time = datetime.now()
    time_passed = end_time - game_start_time
    player.time_to_finish = get_a_str_of_time_in_mn_sec(time_passed)


# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client) -> int:
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1
    return idx


def have_players_finished(players: List[Player]) -> bool:
    for player in players:
        if player.turn < max_turn:
            return False
    return True


def get_a_str_of_time_in_mn_sec(time_passed: float) -> str:
    all_sec = time_passed.total_seconds()
    min = int(all_sec//60)
    only_sec = round(all_sec % 60,2)
    return f'{min} min {only_sec} seconds'

server = start_server()

while True:
    threading._start_new_thread(accept_clients, (server, " "))
print('done')