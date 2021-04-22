
import turtle as t
import random as rand
wn=t.Screen()
fontSetting=font=("System", 20, "normal")
timer=0
counterInterval=1000
timerUp=False
flagCount=10
t.bgcolor("Light Gray")

pen = t.Turtle()
pen.speed(0)
#-----------------------------------------------------------
wn.screensize(360,420)
boardMaker=t.Turtle()
#boardMaker.hideturtle()
boardMaker.penup()
boardMaker.speed(0)

tess=t.Turtle()  
  # self defined function to print coordinate
def buttonclick(x,y): 
    print("You clicked at this coordinate({0},{1})".format(x,y))
  
 #onscreen function to send coordinate
t.onscreenclick(buttonclick,1) 
t.listen()  # listen to incoming connections
t.speed(10) # set the speed
    # hold the screen


pen.penup()
pen.goto(-50.0,318.0)
pen.write("Main Menu", font=("Arial",30,"normal"))

pen.penup()
pen.goto(-361.0,130.0)
pen.write("Player Vs Computer", font=("Arial",25,"normal"))

pen.goto(-62.0,168.0)
pen.down()
pen.left(180)
pen.forward(310)
pen.right(-90)
pen.forward(40)
pen.right(-90)
pen.forward(310)
pen.right(-90)
pen.forward(40)
pen.penup()

pen.goto(242.0,166.0)
pen.down()
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(40)
pen.



pen.penup()
pen.goto(250.0,130.0)
pen.write("Player Vs Player", font=("Arial",25,"normal"))




wn.mainloop()