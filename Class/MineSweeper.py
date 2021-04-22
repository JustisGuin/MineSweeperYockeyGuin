import random as rand
board=[ 
        ["+","1","2","3","4","5","6","7","8","9"],
        ["1"," "," "," "," "," "," "," "," "," "],
        ["2"," "," "," "," "," "," "," "," "," "],
        ["3"," "," "," "," "," "," "," "," "," "],
        ["4"," "," "," "," "," "," "," "," "," "],
        ["5"," "," "," "," "," "," "," "," "," "],
        ["6"," "," "," "," "," "," "," "," "," "],          #This is the board that the Mines and the numbers get placed on 
        ["7"," "," "," "," "," "," "," "," "," "],
        ["8"," "," "," "," "," "," "," "," "," "],
        ["9"," "," "," "," "," "," "," "," "," "]]

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
limit=6
def printBoard(b):  
        for row in range(len(b)):   #for the row in the len of the board
            for col in range(len(b[row])):  #for the col in the len of the board index of the row -1 
                if col !=(len(b[row])-1):   #if the col is not = to the len of the row 
                      print(b[row][col],end=" | ")          #then print in the row and col |
                else:                                   
                      print(b[row][col],end="\n")       #else make a space
            if row !=(len(b)-1):                #if the row is not = to the len then print - 38 times for each row 
                      print("-"*38)
        print()
        for i in range (10):                #looping thru 10 times 
            n=9
            row = rand.randint(1,9)     #getting a random int 1,9 for row 
            col = rand.randint(1,9)     #getting a random int 1,9 for col
            addMark(Mine,row,col,board)     #adding the mine to the row and col 
            # N -->  North        (row-1, col)
            if row > 0:     #if the row is greater than 0 
                if board[row-1][col] in [" ","1","2","3","4","5","6","7","8","9","+","M"]: #This is checking if these strings are there 
                    board[row-1][col]=str(1)                            #If there are there in the north section then add 1 
                else:     
                    print(board[row][col+1])
                    print(row,col)                  
                    board[row-1][col]=str(int(board[row-1][col])+1) #else you are going to add another 
            # S -->  South        (row+1, col)           
            if row < n-1:
                try:
                    if board[row+1][col] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
                        board[row+1][col]=str(1)
                    else:
                        board[row+1][col]=str(int(board[row+1][col])+1)
                except:
                    continue
            # W -->  West         (row, col-1)          
            if col > 0:
                if board[row][col-1] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
                    board[row][col-1]=str(1)
                else:
                    print(board[row][col+1])
                    print(row,col)
                    board[row][col-1]=str(int(board[row][col-1])+1)
            # E -->  East         (row, col+1)     
            if col < n-1:
               if board[row][col+1] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
                    board[row][col+1]=str(1)
               else:
                    print(board[row][col+1])
                    print(row,col)
                    board[row][col+1]=str(int(board[row][col+1])+1)

             #N.W--> North-East   (row-1, col+1)
            
            if row > 0 and col > 0:
                #print(row,col)
                #print(board[row-1][col+1])
                try:

                    if board[row-1][col+1] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
                        board[row-1][col+1]=str(1)
                    
                    else:
                        board[row-1][col+1]=str(int(board[row-1][col+1])+1)
                except:
                    continue
            # N.W--> North-West   (row-1, col-1) 
            if row > 0 and col < n-1:
                #Mine(row-1, col+1)
              #  addMark("O",row-1,col+1,board)
              if board[row-1][col-1] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
                    board[row-1][col-1]=str(1)
              else:
                    print(board[row][col+1])
                    print(row,col)
                    board[row-1][col-1]=str(int(board[row-1][col-1])+1)
            # S.W--> South-West   (row+1, col-1)  
            if row < n-1 and col > 0:
                try:
                        #Mine(row+1, col-1)
                    # addMark("O",row+1,col-1,board)
                    if board[row+1][col-1] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
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
                    if board[row+1][col+1] in [" ","1","2","3","4","5","6","7","8","9","+","M"]:
                            board[row+1][col+1]=str(1)
                    else:
                            board[row+1][col+1]=str(int(board[row+1][col+1])+1)
                except:
                    continue

howToPlay=input("Do you want to see the instructions to play?- ").lower()   #Asking for user Input
if howToPlay == "yes".lower():                          #if the user says "yes" then print this statement 
    print("\nThe numbers on the board represent how many bombs are adjacent to a",
    "\nsquare. For example, if a square has a '3' on it, then there are 3 bombs",
    "\nnext to that square. The bombs could be above, below, right left, or",           
    "\ndiagonal to the square. Avoid all the bombs and expose all the empty",
    "\nspaces to win Minesweeper.\n"
    "\The 0's on the board show there are no bomb around that square."
    "\You will pick either Flag or Step\n")
#flag emoji https://emojipedia.org/triangular-flag/
Flags="🚩"
while Mine!="Q".lower(): #While the  is not Q then continue thru the while loop 
    correctInput = False
    printBoard(board)
    row=int(input("Which row? "))               #This while loop is asking for the user input 
    col=int(input("Which col? "))
    if not((0<=row<=9) and (0<=col<=9)):    #if the row and col is not < or > than 0 and 9 
        print("The row and column are not correct")     #then print 
    elif board[row][col] =="M": #elif the board row and col ="M"
        print("Game Over")  #then print game over
        break                       
    elif board[row][col]!=" ":  #if the space is not = to " " 
        print("That space was already taken")   #then print space taken
    elif board[row][col]!="M":
        print("Game Over you stepped on a Mine")
        break
    else:
        correctInput=True           #change input to true 

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