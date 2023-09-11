board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_state(board):
    for i, c in enumerate(board):
        if (i+1) % 3 ==0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')
            
            
winning_combination = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]


def game(board, combination):
    for (x,y,z) in combination:
        if board[x] == board[y] and board[y] == board[z] and (board[x] == 'X' or board[x] == 'O'):
            return board[x]
    return ''
    

def play_game(board):
    current_sign = 'X'
    while(game(board, winning_combination)==''):
        index = int(input(f'Where do you want draw {current_sign}?'))
        board[index] = current_sign
        
        print_state(board)
        
        winner_sign = game(board, winning_combination)
        
        if winner_sign != '':
            print(f'We have a winner!')
        
        current_sign = 'X' if current_sign == 'O' else 'O'
        