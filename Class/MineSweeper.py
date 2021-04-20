import random as rand
board=[ 
        ["+","A","B","C","D","E","F","G","H","I"],
        ["A"," "," "," "," "," "," "," "," "," "],
        ["B"," "," "," "," "," "," "," "," "," "],
        ["C"," "," "," "," "," "," "," "," "," "],
        ["D"," "," "," "," "," "," "," "," "," "],
        ["E"," "," "," "," "," "," "," "," "," "],
        ["F"," "," "," "," "," "," "," "," "," "],          #This is the board that the Mines and the numbers get placed on 
        ["G"," "," "," "," "," "," "," "," "," "],
        ["H"," "," "," "," "," "," "," "," "," "],
        ["I"," "," "," "," "," "," "," "," "," "]]

def addMark(m,r,c,b):
    #if the space is blank, add that mine
    if b[r][c]==" ":
        b[r][c]=m   
        return True
    return False
#https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
def title():
    print(' ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ')
    print('▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌')
    print('▐░▌░▌   ▐░▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌')
    print('▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌')
    print('▐░▌ ▐░▐░▌ ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌')
    print('▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌')
    print('▐░▌   ▀   ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ')
    print('▐░▌       ▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌                    ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌          ▐░▌     ▐░▌  ')
    print('▐░▌       ▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ')
    print('▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌')
    print(' ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ ')
title()
Mine="M"
numberList=[1,2,3,4,5]
def printBoard(b):
        for row in range(len(b)):
            for col in range(len(b[row])):
                if col !=(len(b[row])-1):
                      print(b[row][col],end=" | ")          #This is the function to print the board I explained this up above 
                else:
                      print(b[row][col],end="\n")
            if row !=(len(b)-1):
                      print("-"*38)
        print()
        for i in range (10):
            n=9
            row = rand.randint(1,9)
            col = rand.randint(1,9)
            addMark(Mine,row,col,board)
            # N -->  North        (row-1, col)
            if row > 0:
                #Mine(row-1, col)
                #addMark("O",row-1,col,board)
                if board[row-1][col] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                    board[row-1][col]=str(1)
                else:
                    board[row-1][col]=str(int(board[row-1][col])+1)
            # S -->  South        (row+1, col)           
            if row < n-1:
                try:
                    #Mine(row+1, col)
                    #addMark("O",row+1,col,board)
                    if board[row+1][col] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                        board[row+1][col]=str(1)
                    else:
                        board[row+1][col]=str(int(board[row+1][col])+1)
                except:
                    continue
            # W -->  West         (row, col-1)          
            if col > 0:
                #Mine(row, col-1)
                #addMark("O",row,col-1,board)
                
                if board[row][col-1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                    board[row][col-1]=str(1)
                else:
                    board[row][col-1]=str(int(board[row][col-1])+1)
            # E -->  East         (row, col+1)     
            if col < n-1:
                #Mine(row, col+1)
               # addMark("O",row,col+1,board)
               if board[row][col+1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                    board[row][col+1]=str(1)
               else:
                    board[row][col+1]=str(int(board[row][col+1])+1)
#  this does not work "IndexError: list index out of range" 
             #N.W--> North-East   (row-1, col+1)
            
            if row > 0 and col > 0:
                #print(row,col)
                #print(board[row-1][col+1])
                try:

                    if board[row-1][col+1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                        board[row-1][col+1]=str(1)
                    
                    else:
                        board[row-1][col+1]=str(int(board[row-1][col+1])+1)
                except:
                    continue
            # N.W--> North-West   (row-1, col-1) 
            if row > 0 and col < n-1:
                #Mine(row-1, col+1)
              #  addMark("O",row-1,col+1,board)
              if board[row-1][col-1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                    board[row-1][col-1]=str(1)
              else:
                    board[row-1][col-1]=str(int(board[row-1][col-1])+1)
            # S.W--> South-West   (row+1, col-1)  
            if row < n-1 and col > 0:
                try:
                        #Mine(row+1, col-1)
                    # addMark("O",row+1,col-1,board)
                    if board[row+1][col-1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                            board[row+1][col-1]=str(1)
                    else:
                            board[row+1][col-1]=str(int(board[row+1][col-1])+1)
                except:
                    continue
            # S.E--> South-East   (row+1, col+1)             
            if row < n-1 and col < n-1:
                try:

                        #Mine(row+1, col+1)
                    #  addMark("O",row+1,col+1,board)
                    if board[row+1][col+1] in [" ","A","B","C","D","E","F","G","H","I","M","+"]:
                            board[row+1][col+1]=str(1)
                    else:
                            board[row+1][col+1]=str(int(board[row+1][col+1])+1)
                except:
                    continue

        #print(col)
        #print(row)
userBoard=[
        ["+","1","2","3","4","5","6","7","8","9"],
        ["1"," "," "," "," "," "," "," "," "," "],
        ["2"," "," "," "," "," "," "," "," "," "],
        ["3"," "," "," "," "," "," "," "," "," "],
        ["4"," "," "," "," "," "," "," "," "," "],
        ["5"," "," "," "," "," "," "," "," "," "],
        ["6"," "," "," "," "," "," "," "," "," "],          #This is the board that the Mines and the numbers 
        ["7"," "," "," "," "," "," "," "," "," "],
        ["8"," "," "," "," "," "," "," "," "," "],
        ["9"," "," "," "," "," "," "," "," "," "]]
    

    
    #secure_random = rand.SystemRandom()
    #res = [int(sub.split('.')[1]) for sub in numberList]
#for when you need to print flags
#print("Flags- {}".format(int(numOfFlags)))
#----- RUNNING CODE -----
howToPlay=input("Do you want to see the instructions to play?- ").lower()
if howToPlay == "yes":
    print("\nThe numbers on the board represent how many bombs are adjacent to a",
    "\nsquare. For example, if a square has a '3' on it, then there are 3 bombs",
    "\nnext to that square. The bombs could be above, below, right left, or",           #These are the instructions for the game and a little user input to see if they want to see if and if they want to play 
    "\ndiagonal to the square. Avoid all the bombs and expose all the empty",
    "\nspaces to win Minesweeper.\n"
    "\The 0's on the board show there are no bomb around that square."
    "\You will pick either Flag or Step\n"
    "The Letter still represent numbers.")
#flag emoji https://emojipedia.org/triangular-flag/
#:triangular_flag_on_post:
Flags=":triangular_flag_on_post:"
while Mine!="Q":
    correctInput = False
    #while not correctInput:
    printBoard(board)
    #Remeber that you need to do action if statments do if action == ui flags then create a if statment
    #do this with flag, col, row
    row=int(input("Which row? "))               #This while loop is asking for the user input 
    col=int(input("Which col? "))
    if not((0<=row<=9) and (0<=col<=9)):
        print("The row and column are not correct")             #This is checking if the game if over to see if you have stepped on a  mine of if you have tried to go some where that a space has been taken
    #try to add a mark, and if you do, this is true.....
    elif board[row][col] =="M":
        print("Game Over")
        break               
    elif board[row][col]!=" ":
        print("That space was already taken")
    else:
        correctInput=True
"""
So the thing we dont have is when you pick the row and the col the numbers 
Add up also when you ask to go somewhere if places a M in the place of where you want to go. 
"""
"""
This will help with the algoritm to check 
Cell-->Current Cell (row, col) 
        N -->  North        (row-1, col) 
        S -->  South        (row+1, col) 
        E -->  East         (row, col+1) 
        W -->  West            (row, col-1) 
        N.E--> North-East   (row-1, col+1) 
        N.W--> North-West   (row-1, col-1) 
        S.E--> South-East   (row+1, col+1) 
        S.W--> South-West   (row+1, col-1)
"""