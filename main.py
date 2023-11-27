import turtle
import time
sleep = time.sleep
screen = turtle.Screen()
king = turtle.Turtle()
sp = turtle.Turtle()
btn1 = turtle.Turtle()
dvt = turtle.Turtle()

#Setup
grey = "pygrey.jpg"
kingg = "Kingofsteak3.jpg"
start = "canvas.jpg"
creds = "Creds.jpg"
screen.setup(650,500, 0, 0)
screen.bgcolor("grey")

#pics
screen.addshape(grey)
screen.addshape(creds)
screen.addshape(start)
screen.addshape(kingg)
#turtles
btn1.shape(start)
king.shape(kingg)
king.penup()
king.speed(0)
king.left(90)




move_speed = 10
turn_speed = 10
#Title Screen
sp.hideturtle()
sp.penup()
sp.speed(0)
sp.goto(-150,200)
sp.write("King Of Steak" , "center", font=("Arial", 35, "normal"))


#btn1
btn1.penup()
btn1.speed(0)
btn1.goto(0,-200)
btn1.left(90)
def clk(x,y):
  btn1.hideturtle()
  btn1.goto(1000000,1000000)
  dvt.clear()
  dvt.done()
  sp.clear()
  king.hideturtle()
  import Game
btn1.onclick(clk)
#mini secret-----------------------------------------
def fd():
  king.forward(move_speed)
  ycors = king.ycor()
  xcors = king.xcor()
  if xcors <= -216: 
    king.backward(move_speed)
  if xcors >= 138:
    king.backward(move_speed)
  if ycors <= -220:
    king.backward(move_speed)
  if ycors >= 220:
    king.backward(move_speed)
def lf():
  king.left(turn_speed)
def bwrd():
  king.backward(move_speed)
  ycorm = king.ycor()
  xcorm = king.xcor()
  if xcorm <= -216: 
    king.forward(move_speed)
  if xcorm >= 138:
    king.forward(move_speed)
  if ycorm <= -220:
    king.forward(move_speed)
  if ycorm >= 220:
    king.forward(move_speed)
def rt():
  king.right(turn_speed)

#dev tools------------------------------------------
dvt.shape(grey)
#dvt.hideturtle()
dvt.penup()
dvt.speed(0)
dvt.goto(200,230)
dvt.write("Version Alpha 1.5       ", "center", font=("Arial", 9, "normal"))
def dt(x,y):
  dev = input()
  dev = dev.lower()
  if dev == 'hispanic rice is the best':
    print("Dev Tools Activated")
    print("What file would you like to skip to? C/R/W/B/O")
    imp = input()
    imp = imp.upper()
    if imp == 'C':
      print("Importing...")
      btn1.hideturtle()
      btn1.goto(1000000,1000000)
      sp.clear()
      king.hideturtle()
      import credits
    elif imp == 'R':
      print("Importing...")
      btn1.hideturtle()
      btn1.goto(1000000,1000000)
      sp.clear()
      king.hideturtle()
      import raw
    elif imp == 'W':
      print("Importing...")
      btn1.hideturtle()
      btn1.goto(1000000,1000000)
      sp.clear()
      king.hideturtle()
      import w
    elif imp == 'B':
      print("Importing...")
      btn1.hideturtle()
      btn1.goto(1000000,1000000)
      sp.clear()
      king.hideturtle()
      import burnt
    elif imp == 'O':
      print("Importing...")
      btn1.hideturtle()
      btn1.goto(1000000,1000000)
      sp.clear()
      king.hideturtle()
      import oof
    else:
      print("ERROR CODE 400")
  elif dev == 'asian rice is the best':
    print("Who the hell are you, go away.")
    exit()
  elif dev == 'fried rice is the best':
    print("NOPE. NUH UH. GO THE FUDGE AWAY.")
    exit()
dvt.onclick(dt)
    
  


screen.onkey(fd, "w")
screen.onkey(lf, "a")
screen.onkey(bwrd, "s")
screen.onkey(rt, "d")
screen.listen()








