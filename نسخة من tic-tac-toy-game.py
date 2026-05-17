
import random

board = [[1,2,3],[4,5,6],[7,8,9]]



def display_board():
    def looking(): 
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   "+ str(board[0][0]) +"   "+"|   "+str(board[0][1])+"   |" + "   "+str(board[0][2])+"   |")
        print("|       "*3 + "|")
    def looking1(): 
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   "+str(board[1][0])+"   "+"|   "+str(board[1][1])+"   |" + "   "+str(board[1][2])+"   |")
        print("|       "*3 + "|")
    def looking3(): 
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   "+str(board[2][0])+"   "+"|   "+str(board[2][1])+"   |" + "   "+str(board[2][2])+"   |")
        print("|       "*3 + "|")

    looking()
    looking1()
    looking3()
    
    print("+-------"*3 + "+")
board[1][1] = "X"




def make_list_of_free_fields(board):
    free=[]
    for row in range(3):
     for col in range(3):
        if board[row][col] != "X" and board[row][col] != "O":
           free.append((row,col))

    return free



def victory_for(board, sign):

    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        
        return True

    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
       
        return True

    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        
        return True

    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
       
        return True

    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        
        return True

    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        
        return True

    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        
        return True

    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        
        return True

    return False



def enter_move():
   mapping = [
       (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2)
   ]
    
   firstnum = (int(input("Welcome to the game, inter the first number: ")))

   first_answer = int(firstnum)


   if first_answer <1 or first_answer >9 :
       print ("not avilabel number")
       return
   
   (row,col)=mapping[first_answer-1]



   if board[row][col]== "X" or board[row][col]== "O":
        print("this move is not available")
   else:
        board[row][col] = "O"


def draw_move(board):
  
  free=make_list_of_free_fields(board)

  row,col = random.choice(free)

  board[row][col]="X"
   
   

    

while True:

    display_board()

    enter_move()

    if victory_for(board, "O"):
        print("O wins")
        break

    draw_move(board)

    if victory_for(board, "X"):
        print("X wins")
        break



