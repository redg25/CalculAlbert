#Methods to perform CLI displayy

def client_receive_welcome(value):
    if value['nb_of_players']=='1':
        print(f'Welcome {value}')
        print('Waiting for another player...\n'
              'Press "q" to quit\n')
    elif value['nb_of_players']=='2':
        print(f'Welcome {value}')


def client_receive_wait(value):
    print(f'Game will start in {value} seconds...')


def client_receive_operation(value):
    while True:
        my_answer = input(value['op_str'])
        if str(my_answer) == str(value['res']):
            score = 1
            request = dict(score=score)
            return request
        else:
            print('Wrong answer\n'
                  'Please try again...')



def client_receive_end_game(value):
    print(value['message'])


def client_receive_final(value):
    for score in value['scores']:
        print(f'{score} has {value["scores"][score][0]} in {value["scores"][score][1]}')