import random
import itertools

#ADD
'''
score
game over check
'''
SIZE = 4
LIMIT = 2048

board = [[0 for i in range(SIZE)] for i in range(SIZE)]

def add_num(board, size, limit):
    for i,j in itertools.product(range(size), range(size)):
        if board[i][j] == limit:
            print('You win!')
            return True

    x = random.randrange(size)
    y = random.randrange(size)

    if board[x][y] == 0: board[x][y] = 2
    else: add_num(board, size, limit)

    return False
    
def move(board, score, size):
    curr_board = [x[:] for x in board]
    user_input = input('U/D/L/R: ').upper()

    if user_input == 'U':
        for x,y in itertools.product(range(1,size), range(size)):
            count = x
            while count > 0:
                if board[count][y] != 0 and board[count-1][y] == 0:
                    board[count-1][y] = board[count][y]
                    board[count][y] = 0
                elif board[count][y] == board[count-1][y] and board[count][y] != 0:
                    score += board[count-1][y]
                    board[count-1][y] *= 2
                    board[count][y] = 0
                    count = 0
                count -= 1

    elif user_input == 'D':
        for x,y in itertools.product(range(2,5), range(4)):
            count = -x
            while count < -1:
                if board[count][y] != 0 and board[count+1][y] == 0:
                    board[count+1][y] = board[count][y]
                    board[count][y] = 0
                elif board[count][y] == board[count+1][y] and board[count][y] != 0:
                    score += board[count+1][y]
                    board[count+1][y] *= 2
                    board[count][y] = 0
                    count = 0
                count += 1

    elif user_input == 'L':
        for x,y in itertools.product(range(size), range(1,size)):
            count = y
            while count > 0:
                if board[x][count] != 0 and board[x][count-1] == 0:
                    board[x][count-1] = board[x][count]
                    board[x][count] = 0
                elif board[x][count] == board[x][count-1] and board[x][count] != 0:
                    score += board[x][count-1]
                    board[x][count-1] *= 2
                    board[x][count] = 0
                    count = 0
                count -= 1

    elif user_input == 'R':
        for x,y in itertools.product(range(4), range(2,5)):
            count = -y
            while count < -1:
                if board[x][count] != 0 and board[x][count+1] == 0:
                    board[x][count+1] = board[x][count]
                    board[x][count] = 0
                elif board[x][count] == board[x][count+1] and board[x][count] != 0:
                    score += board[x][count+1]
                    board[x][count+1] *= 2
                    board[x][count] = 0
                    count = 0
                count += 1             
                    
    else:
        print('Please enter a valid argument.\n')
        move(board, score, size)

    if curr_board == board:
        print('Please enter a valid argument.\n')
        move(board, score, size)
    
    return score
    
def main():
    no_space = False
    score = 0
    
    while no_space == False:
        try:
            no_space = add_num(board, SIZE, LIMIT)
            [print('{}'.format(board[n])) for n in range(SIZE)]
            print('------------\nScore: {}\n------------'.format(score))
            score = move(board, score, SIZE)
                
        except:
            no_space = True

if __name__ == '__main__':
    main()
