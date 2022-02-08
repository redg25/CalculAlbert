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
    name: str = None
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
    print (socket.AF_INET)
    print (socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection
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


def are_players_ready() -> bool:
    all_players_have_names = True
    for player in players:
        if player.name == None:
            all_players_have_names = False
            break

    return (game_turn == 1) and len(players) == 2 and all_players_have_names

def add_name_to_player(sock, name):
    for player in players:
        if player.client == sock:
            player.name = name
            break

def send_receive_client_message(client_connection,addr):
    global game_started, game_turn,players, game_start_time
    global operations
    while True:
        try:
            current_player = get_player_from_client(client_connection)
            if are_players_ready():
                print(f'Players are ready to play...')
                game_started = True
                for player in players:
                    send_new_request(player.client,'wait','3')
                sleep(3)
                value = start_a_game()
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
                    add_name_to_player(client_connection,value)
                    print(f"{message.addr} sent a player name: {value}")
                    if len(players) == 1:
                        request_value = dict(nb_of_players='1')
                        send_new_request(client_connection,'welcome',request_value)
                    elif len(players) == 2:
                        request_value = dict(nb_of_players='2')
                        send_new_request(client_connection,'welcome',request_value)
                elif action == 'start':
                    c = Calcul(50,3,['+','*'],[10])
                    new_op_str,res = c.make_operation()
                    operations.append((new_op_str,res))
                    value = {'op_str':new_op_str,'res':res}
                    for player in players:
                        send_new_request(player.client,'operation',value)
                elif action == 'answer':
                    print('Server here')
                    player = get_player_from_client(client_connection)
                    player.score += value['score']
                    player.turn +=1
                    print (operations,player.turn)
                    if player.turn == max_turn:
                        end_time = datetime.now()
                        time_passed = end_time - game_start_time
                        player.time_to_finish = get_a_str_of_time_in_mn_sec(time_passed)
                    if player.turn == max_turn and not have_players_finished(players):
                        value = dict(score=current_player.score,message="Please wait for your opponent to finish")
                        send_new_request(client_connection,'end_game',value)
                    elif have_players_finished(players):
                        ls_of_results = {}
                        for player in players:
                            ls_of_results[player.name]=[player.score,player.time_to_finish]
                        for player in players:
                            value = dict(scores=ls_of_results)
                            send_new_request(player.client,'final',value)
                    elif len(operations)<player.turn:
                        print(f'{player.name} is the first player to play for the question {player.turn}')
                        value = start_a_game()
                        send_new_request(player.client,'operation',value)
                        game_turn += 1
                    else:
                        print(f'{player.name} is the second player to play for the question {player.turn}')
                        operation = operations[player.turn -1]
                        value = {'op_str':operation[0],'res':operation[1]}
                        send_new_request(player.client,'operation',value)
                    print(f'{player.name} score is {player.score}')

        except Exception as e:
            print(e)
            break
    client_connection.close()

def get_player_from_client(client)-> Player:
    for player in players:
        if player.client == client:
            return player

# Return the index of the current client in the list of clients
def start_a_game():
    c = Calcul(50,3,['+','*'],[10])
    new_op_str,res = c.make_operation()
    operations.append((new_op_str,res))
    value = {'op_str':new_op_str,'res':res}
    return value


def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx

def have_players_finished(players)-> bool:
    for player in players:
        if player.turn < max_turn:
            return False
    return True

def get_a_str_of_time_in_mn_sec(time_passed):
    all_sec = time_passed.total_seconds()
    min = int(all_sec//60)
    only_sec = round(all_sec % 60,2)
    return f'{min} min {only_sec} seconds'

server = start_server()

while True:
    threading._start_new_thread(accept_clients, (server, " "))
print('done')