import random as rand
board=[
        ["+","1","2","3","4","5","6","7","8","9"],
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
def printBoard(b):  #todo explain print board in comments 
        for row in range(len(b)):
            for col in range(len(b[row])):
                if col !=(len(b[row])-1):
                      print(b[row][col],end=" | ")
                else:
                      print(b[row][col],end="\n")
            if row !=(len(b)-1):
                      print("-"*38)
        print()


def addMark(m,r,c,b):
    #if the space is blank, add that mine
    if b[r][c]==" ":
        b[r][c]=m
        return True
    return False
for i in range (11):
    row = rand.randint(1,9)
    col = rand.randint(1,9)
    addMark(Mine,row,col,board)

printBoard(board)

for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]=="M":
                    print(row,col)
                      
    