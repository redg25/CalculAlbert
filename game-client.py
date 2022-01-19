import socket
from process_request_client import Message

# network client
HOST_ADDR = "127.0.0.1"
HOST_PORT = 8080


def create_request(action, value):
    return dict(
        type="text/json",
        encoding="utf-8",
        content=dict(action=action, value=value),
    )


def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST_ADDR, HOST_PORT))
    player_name = input("What's your name?\n")
    send_new_request(client,'name',player_name)
    receive_message_from_server(client, "m")


def send_new_request(client,action,value):
    request = create_request(action,value)
    message = Message(client,(HOST_ADDR,HOST_PORT))
    message.request = request
    message.process_events('w')


def receive_message_from_server(client, m):
    while True:
        try:
            message = Message(client,(HOST_ADDR,HOST_PORT))
            message.process_events('r')
            action = message.response['action']
            value = message.response['value']
            if action == 'welcome':
                if value['nb_of_players']=='1':
                    print(f'Welcome {value}')
                    print('Waiting for another player...\n'
                                   'Press "q" to quit\n')
                elif value['nb_of_players']=='2':
                    print(f'Welcome {value}')
            elif action == 'wait':
                print(f'Game will start in {value} seconds...')
            elif action == 'operation':
                input(value['op_str'])
        except Exception as e:
            print(e)
            break


connect_to_server()



