import random as rand
# Beginner Game Mode
def beginnerMode():
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
        row = rand.choice(board[1:])
        col = rand.choice(row[1:])
        #board=rand.choice[row:col:]
        if board[row][col]==" ":
            rand.randint()
        
        print(col)
        print(row)
    printBoard(board)
    



print("Welcome to Minesweeper")
print("The numbers on the board represent how many bombs are adjacent to a square.",
"For example, if a square has a '3' on it, then there are 3 bombs next to that square.",
" The bombs could be above, below, right left, or diagonal to the square. Avoid all",
"the bombs and expose all the empty spaces to win Minesweeper.")
gamemode=input("Are you ready?- ").lower()
while gamemode != ("yes"):
    gamemode=input("Are you ready?- ").lower()
beginnerMode()







