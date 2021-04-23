import turtle as t    #importing turtle   
import random as rand
wn=t.Screen()
t.bgcolor("Light Gray")
pen = t.Turtle()  #making each turtle for each function 
play = t.Turtle()
comp = t.Turtle()
wn.screensize(600,600)    #allowing the screen to be a certain size 
#-----------------------------------------------------------

#Functions 

def computer():     
  pen.hideturtle()    #This is hiding the turtle      
  comp.hideturtle()
  play.hideturtle()
  #wn.clear()
  pen.clear() 
  comp.clear()#This is for the clear functions down below to allow it to clear   
  play.clear()
  wn.bgcolor("Light Gray")    #changing the bg color to light gray 
  comp.penup()
  comp.goto(-75,308.0)
  comp.write("Directions",font=("Arial",30,"normal")) 
  comp.goto(-350,108.0)
  #Got the "Offical" Rules for Minesweeper at https://www.ducksters.com/games/minesweeper.php#:~:text=The%20numbers%20on%20the%20board,empty%20spaces%20to%20win%20Minesweeper.
  comp.write("The numbers on the board represent how many bombs are adjacent to a square.\nFor example, if a square has a 3 on it, then there are 3 bombs next to that square.\nThe bombs could be above, below, right left, or diagonal to the square.\n Avoid all the bombs and expose all the empty spaces to win Minesweeper",font=("Arial",18,"normal"))

  comp.goto(275,350.0)
  comp.write("Press g to play Computer Vs Computer Minesweeper",font=("Arial",18,"normal"))



  comp.goto(-300,350.0)
  comp.write("Press e to exit",font=("Arial",18,"normal"))
  


def player():
  wn.bgcolor("Light Gray")
  #wn.clear()
  pen.hideturtle() #Hiding the turtles 
  comp.hideturtle()
  play.hideturtle()
  pen.clear() 
  comp.clear()
  play.clear()#This is for the clear functions down below to allow it to clear   
  play.penup()
  play.goto(-75,308.0)
  play.write("Directions",font=("Arial",30,"normal"))             #Writing on the screen 
  play.goto(-300,108.0)
  play.write("In this style of the game you will be facing off with another player.\n The first player in the game will have to finsh MineSweeper the fastest they can!\n",font=("Arial",18,"normal"))

  play.write("Then the second player will have to try to beat the first players time.",font=("Arial",18,"normal"))

  
  play.goto(-300,350.0)
  play.write("Press e to exit",font=("Arial",18,"normal"))
  

def clear():

    #wn.clear()

    pen.clear() 
    comp.clear()      #This is clearing the screen and going back to main menu 
    play.clear()
    mainMenu()


#def playComputer(): Waiting for Gui to be done 
    


def mainMenu():
    global pen    #Allowing pen to be accessed
    pen.speed(0)
    wn.bgcolor("Light Gray")              
    pen.penup()
    pen.goto(-50.0,308.0)
    pen.write("Main Menu", font=("Arial",30,"normal"))      #Making the main menu text 

    pen.penup()
    pen.goto(-361.0,130.0)      #Going to an exact cord for x and y to write on screen 
    pen.write("Player Vs Computer", font=("Arial",25,"normal"))     

    pen.goto(-371.0,100.0)
    pen.write("Press c to see Player Vs Computer Directions",font=("Arial",15,"normal"))

    pen.penup()
    pen.goto(250.0,130.0)
    pen.write("Player Vs Player", font=("Arial",25,"normal"))

    pen.goto(250.0,100.0)
    pen.write("Press p to see Player vs Player Directions",font=("Arial",15,"normal"))

    pen.goto(250.0,130.0)
    pen.write("Player Vs Player", font=("Arial",25,"normal")) 
    
    pen.goto(-371.0,50)
    pen.write("Press g to play Computer Vs Computer Minesweeper",font=("Arial",15,"normal"))


#-------------------------------------------------------------------------------------------------------------------------
mainMenu()    #Allowing the main menu to be showing 


wn.onkeypress(computer, 'c')      #Key binds to let you go to other screens 
wn.onkeypress(player, 'p')
wn.onkeypress(clear,"e")
#wn.onkeypress(playComputer,"g")

wn.listen()   #allowing the keybinds to work 

wn.mainloop() 