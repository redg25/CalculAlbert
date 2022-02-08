import socket
from process_request_client import Message
import client_screen_action

# network client
HOST_ADDR = "127.0.0.1"
HOST_PORT = 8080

# Mapping of methods to call based on requests received from server
screen_actions:dict = {'welcome':'client_receive_welcome',
                       'wait':'client_receive_wait',
                       'operation':'client_receive_operation',
                       'end_game':'client_receive_end_game',
                       'final':'client_receive_final'}

# Mapping of request names to send back to server based on requests received from server
send_back_request:dict = {'operation':'answer'}


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
            #Get method to call based on request from server
            action_method_to_call = getattr(client_screen_action,screen_actions[action])
            request_to_send = action_method_to_call(value)
            #Send a request back if necessary
            if request_to_send:
                action_to_server = send_back_request[action]
                send_new_request(client,action_to_server,request_to_send)
        except Exception as e:
            print(e)
            break


connect_to_server()



