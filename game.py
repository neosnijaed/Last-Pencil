import random


def get_numeric_value():
    try:
        num_pencils = int(input())
    except ValueError:
        print('The number of pencils should be numeric')
        return False
    else:
        if num_pencils < 0:
            print('The number of pencils should be numeric')
            return False
        else:
            return num_pencils


def get_positive_value(num_pencils: int):
    if num_pencils == 0:
        print('The number of pencils should be positive')
        return False
    else:
        return num_pencils


def get_pencils():
    numeric_value = get_numeric_value()
    if numeric_value is False:
        return get_pencils()
    else:
        positive_value = get_positive_value(numeric_value)
        if positive_value is False:
            return get_pencils()
        else:
            return positive_value


def get_player():
    player_name = input()
    if player_name not in ['John', 'Jack']:
        print('Choose between \'John\' and \'Jack\'')
        return get_player()
    else:
        return player_name


def get_draw_pencils():
    num_pencils = input()
    if num_pencils not in ['1', '2', '3']:
        print('Possible values: \'1\' and \'2\' and \'3\'')
        return get_draw_pencils()
    else:
        return int(num_pencils)


def check_pencils_taken(num_pencils: int, draw_pencils: int):
    if draw_pencils > num_pencils:
        draw_pencils = int(input('Too many pencils were taken\n'))
        return check_pencils_taken(num_pencils, draw_pencils)
    else:
        return draw_pencils


def play_bot(num_pencils: int):
    if num_pencils == 1:
        return 1
    remaining_value = num_pencils % 4
    if remaining_value == 0:
        return 3
    elif remaining_value == 3:
        return 2
    elif remaining_value == 2:
        return 1
    else:
        return random.randint(1, 3)


print('How many pencils would you like to use:')
n_pencils = get_pencils()
print('Who will be the first (John, Jack):')
players_turn = get_player()
print('|' * n_pencils)
while n_pencils > 0:
    print(f'{players_turn}\'s turn!')
    take_pencils = 0
    if players_turn == 'John':
        take_pencils = get_draw_pencils()
        take_pencils = check_pencils_taken(n_pencils, take_pencils)
    elif players_turn == 'Jack':
        take_pencils = play_bot(n_pencils)
        print(take_pencils)
    n_pencils -= take_pencils
    players_turn = 'John' if players_turn == 'Jack' else 'Jack'
    if n_pencils == 0:
        print(f'{players_turn} won!')
        break
    print('|' * n_pencils)
