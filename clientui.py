from appclient import *

message = start_client("127.0.0.1",8000,"new","")
answer = input(message.response['op_string'])
# message = start_client("127.0.0.1",8000,"answer","1")
# answer = input(message.response['op_string'])
while True:
    if answer == message.response['result']:
        message = start_client("127.0.0.1",8000,"answer","1")

    else:
        message = start_client("127.0.0.1",8000,"answer","0")
    if message.response['op_string'] == "end":break
    else:
        answer = input(message.response['op_string'])

print(f'you score is {message.response["result"]}')


