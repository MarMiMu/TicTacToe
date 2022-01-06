import random
import math 
def display_board(board):
    print(" "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", board[0][0] ," ","|"," ", board[0][1] ," ","|"," ", board[0][2] ," ")
    print(" "," "," ","|"," "," "," ","|"," "," "," ")
    print("---------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", board[1][0] ," ","|"," ", board[1][1] ," ","|"," ", board[1][2] ," ")
    print(" "," "," ","|"," "," "," ","|"," "," "," ")
    print("---------------------")
    print(" "," "," ","|"," "," "," ","|"," "," "," ")
    print(" ", board[2][0] ," ","|"," ", board[2][1] ," ","|"," ", board[2][2] ," ")
    print(" "," "," ","|"," "," "," ","|"," "," "," ")

def do_move(board,player):
    if (player == "X"):
        pos = int(input("Player "+player+" Which position (1-9) do you want to go?:")) 
        if (update_board(board,pos,player)):
            display_board(board)
        else:
            print("Position occupied, select new position")
            do_move(board,player)
    else:
        ai_move(board)
        display_board(board) 


def ai_move(board):
    best_score = -999999
    best_move = 0
    valids = get_valid(board)
    alpha = -999999
    beta = 999999
    depth = 1 
    for i in valids:
        update_board(board,i,"O")
        score = minimax(board,depth,alpha,beta,False)
        update_board(board,i,str(i))
        if (score > best_score):
            best_score = score
            best_move = i
    update_board(board,best_move,"O")   
    

def minimax(board,depth,alpha,beta,isMaximizing):
    winner = win_condition(board)
    draw = draw_condition(board)
    valids = get_valid(board)
    if (winner == "X"):
        return -1
    elif (winner == "O"):
        return 1
    elif (winner == False and draw == True):
        return 0
    else:
        if (isMaximizing):
            best_score = -999999
            for i in valids:
                update_board(board,i,"O")
                score = minimax(board,depth + 1,alpha,beta,False)
                update_board(board,i,str(i))
                best_score = max(best_score,score)
                alpha = max(alpha,score)
                if beta <= alpha:
                    break
        else:
            best_score = 999999
            for i in valids:
                update_board(board,i,"X")
                score = minimax(board,depth + 1,alpha,beta,True)
                update_board(board,i,str(i))
                best_score = min(best_score,score)
                beta = min(beta,score)
                if beta <= alpha:
                    break
    return best_score 
            
            

def get_valid(board):
    valid_locations = []
    for i in range(1,10):
        row = int((i-1)/3)
        col = (i-1)%3
        if board[row][col] != "X" and board[row][col] != "O":
            valid_locations.append(i)
    return valid_locations


            
def update_board(board,pos,char):
    row = int((pos-1)/3)
    col = (pos-1)%3
    if (board[row][col] == "X" and char == "O") or (board[row][col] == "O" and char == "X"):
        return False
    board[row][col] = char
    return True 

def win_condition(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[2][2]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return False

def draw_condition(board):
    for i in range(3):
        for j in range(3):
            if not (board[i][j] == "X" or board[i][j] == "O"):
                return False
    return True

def game_over(board):
    result = win_condition(board) or draw_condition(board)
    if result != False:
        return True
    else:
        return False

def game():
    board = ["1","2","3"],["4","5","6"],["7","8","9"]
    player = ""
    player1 = "X"
    player2 = "O"
    move_counter = 0
    status = game_over(board)
    while (status == False):
        if (move_counter%2 == 1):
            player = player2
        else:
            player = player1
        do_move(board,player)
        status = game_over(board)
        print(status)
        move_counter += 1
    if (win_condition(board) == False):
        print("No winner - The game is drawn")
    else:
        print("Winner is,", player)
