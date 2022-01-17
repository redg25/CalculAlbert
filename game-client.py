

import socket
from time import sleep
import threading
from process_request_client import Message

# network client
client = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 8080

def create_request(action, value):
    if action == "name":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )

    else:
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action="temp", value="temp"),
        )

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client.connect_ex((HOST_ADDR,HOST_PORT))
        client.connect((HOST_ADDR, HOST_PORT))
        request = create_request("name",name)
        message = Message(client,(HOST_ADDR,HOST_PORT),request)
        message.process_events('w')
        # client.send(name.encode()) # Send name to server after connecting
        print('sent name to server')

        # disable widgets


        # start a thread to keep receiving message from server
        # do not block the main thread :)
        #threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        print(e)

second = False

var = False
def receive_message_from_server(sck, m):
    global your_name, opponent_name, game_round,second
    global your_choice, opponent_choice, your_score, opponent_score

    while True:
        if second == False:
            second = True
            request = create_request("name",'jean')
            message = Message(client,(HOST_ADDR,HOST_PORT),request)
            message.process_events('w')


        data = sck.recv(4096)

        if not data: break

        if data == b'welcome1':
            print(data)
            action = input('new action: ')
            client.send(action.encode())
        else:
            print(data)






connect_to_server('regis')
while True:
    if var == False:
        sleep(5)
        var = True

    threading._start_new_thread(receive_message_from_server, (client, "m"))

