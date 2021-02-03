import random as rand


#----- FUNCTIONS -----

#randomly addes the mine in
def addMark(m,r,c,b):
    #if the space is blank, add that mine
    if b[r][c]==" ":
        b[r][c]=m
        return True
    return False

# Beginner Game Mode

def beginnerMode():
    #^^^^^^^^^^^^^^^
    #Going to to this into a class later
    board=[
        [" ","A","B","C","D","E","F","G","H","I"],
        ["1"," "," "," "," "," "," "," "," "," "],
        ["2"," "," "," "," "," "," "," "," "," "],
        ["3"," "," "," "," "," "," "," "," "," "],
        ["4"," "," "," "," "," "," "," "," "," "],
        ["5"," "," "," "," "," "," "," "," "," "],
        ["6"," "," "," "," "," "," "," "," "," "],
        ["7"," "," "," "," "," "," "," "," "," "],
        ["8"," "," "," "," "," "," "," "," "," "],
        ["9"," "," "," "," "," "," "," "," "," "]]
    Mine="M"
    numberList=[1,2,3,4,5]
    def printBoard(b):
        for row in range(len(b)):
            for col in range(len(b[row])):
                if col !=(len(b[row])-1):
                      print(b[row][col],end=" | ")
                else:
                      print(b[row][col],end="\n")
            if row !=(len(b)-1):
                      print("-"*38)
        print()
    for i in range (10):
        row = rand.randint(1,9)
        col = rand.randint(1,9)
        addMark(Mine,row,col,board)
        #print(col)
        #print(row)
    printBoard(board)
    newboard=[]
    #secure_random = rand.SystemRandom()
    #res = [int(sub.split('.')[1]) for sub in numberList]
    for i in range (10):
        row = rand.randint(1,9)
        col = rand.randint(1,9)
        addMark(rand.choice(numberList),row,col,board)
    printBoard(board)
        #print(col)
        #print(row)
    
    


#----- RUNNING CODE -----
print("Welcome to Minesweeper\n")
howToPlay=input("Do you want to see the instructions to play?- ").lower()
if howToPlay == "yes":
    print("\nThe numbers on the board represent how many bombs are adjacent to a",
    "\nsquare. For example, if a square has a '3' on it, then there are 3 bombs",
    "\nnext to that square. The bombs could be above, below, right left, or",
    "\ndiagonal to the square. Avoid all the bombs and expose all the empty",
    "\nspaces to win Minesweeper.\n")
print("The 0's on the borad show there are no bomb around that square.\n")
gamemode=input("Are you ready?- ").lower()
while gamemode != "yes":
    gamemode=input("Are you ready?- ").lower()

while beginnerMode!="You Have Won" or "You have Lost":
    
    columnsAndRowsInput=input("Enter row and column number to select a cell, Example (1 1)")

beginnerMode()







