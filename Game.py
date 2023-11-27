import turtle
import time
import random
sleep = time.sleep
screen = turtle.Screen()
stove = turtle.Turtle()
circ1 = turtle.Turtle()
circ2 = turtle.Turtle()
circ3 = turtle.Turtle()
circ4 = turtle.Turtle()

#vars
Ethan = 0
Ayden = 1
Harrison = 1000
Lol1 = 0
Lol2 = 0
Lol3 = 0
Lol4 = 0
C = [7, 6.5, 4, 6, 5]
B = [1.3,1,]

c1 = random.choice(C)
c2 = random.choice(C)
c3 = random.choice(C)
c4 = random.choice(C)
b1 = random.choice(B)
b2 = random.choice(B)
b3 = random.choice(B)
b4 = random.choice(B)

#Setup
red = "red.jpg"
rpty = "rpty.jpg"
stov = "grill.jpg"
mrpty = "mrpty.jpg"
bpty = "burnt.jpg"

#pics
screen.addshape(red)
screen.addshape(bpty)
screen.addshape(stov)
screen.addshape(rpty)
screen.addshape(mrpty)
#turtles
stove.shape(stov)
#circ1
circ1.shape(red)
circ1.penup()
circ1.speed(0)
circ1.goto(-90,120)
circ1.left(90)
#circ2 
circ2.shape(red)
circ2.penup()
circ2.speed(0)
circ2.goto(150,130)
circ2.left(90)
#circ3
circ3.shape(red)
circ3.penup()
circ3.speed(0)
circ3.goto(-120,-130)
circ3.left(90)
#circ4
circ4.shape(red)
circ4.penup()
circ4.speed(0)
circ4.goto(120,-130)
circ4.left(90)
#grill
stove.speed(0)
stove.left(90)

#make raw patty appear
#Steak 1
def aper1(x,y):
  circ1.shape(rpty)
  sleep(0.5)
  while True:
    global Lol1
    #raw------------------
    def BENZOS(x,y):
      global Lol1
      Lol1 = int(Lol1) - int(Harrison)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      sleep(0.5)
      import raw
    circ1.onclick(BENZOS)
    sleep(c1)
    #Perfect-----------------
    circ1.shape(mrpty)
    def CHRISSY(x,y):
      global Lol1
      global Ethan
      Lol1 = int(Lol1) - int(Harrison)
      Ethan = int(Ethan) + int(Ayden)
      circ1.goto(1000,1000)
      while True:
        if Ethan == 4:
          stove.penup()
          stove.speed(0)
          stove.goto(1000,1000)
          import w
          Ethan = int(Ethan) - int(Ethan)
    circ1.onclick(CHRISSY)
    sleep(b1)
    #Burnt----------------------------
    circ1.shape(bpty)
    Lol1 = int(Lol1) + int(Ayden)
    if Lol1 == 1:
      sleep(1.5)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      import burnt
    break
    
circ1.onclick(aper1)
#Steak 2 -----------------------------------------------
def aper2(x,y):
  circ2.shape(rpty)
  sleep(0.5)
  while True:
    global Lol2
    #raw------------------
    def BENZOS(x,y):
      global Lol2
      Lol2 = int(Lol2) - int(Harrison)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      sleep(0.5)
      import raw
    circ2.onclick(BENZOS)
    sleep(c2)
    circ2.shape(mrpty)
    #Perfect--------------------
    def AYDEN(x,y):
      global Lol2
      global Ethan
      Lol2 = int(Lol2) - int(Harrison)
      Ethan = int(Ethan) + int(Ayden)
      circ2.goto(1000,1000)
      while True:
        if Ethan == 4:
          stove.penup()
          stove.speed(0)
          stove.goto(1000,1000)
          import w
          Ethan = int(Ethan) - int(Ethan)
    circ2.onclick(AYDEN)
    sleep(b2)
    #Burnt----------------------------
    circ2.shape(bpty)
    Lol2 = int(Lol2) + int(Ayden)
    if Lol2 == 1:
      sleep(1.5)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      import burnt
    break
circ2.onclick(aper2)
#Steak 3 -----------------------------------------------
def aper3(x,y):
  circ3.shape(rpty)
  sleep(0.5)
  while True:
    global Lol3
    #raw------------------
    def BENZOS(x,y):
      global Lol3
      Lol3 = int(Lol3) - int(Harrison)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      sleep(0.5)
      import raw
    circ3.onclick(BENZOS)
    sleep(c3)
    circ3.shape(mrpty)
    #Perfect--------------------
    def Nightwaves(x,y):
      global Ethan
      global Lol3
      Lol3 = int(Lol3) - int(Harrison)
      Ethan = int(Ethan) + int(Ayden)
      circ3.goto(1000,1000)
      while True:
        if Ethan == 4:
          stove.penup()
          stove.speed(0)
          stove.goto(1000,1000)
          import w
          Ethan = int(Ethan) - int(Ethan)
    circ3.onclick(Nightwaves)
    sleep(b3)
    #Burnt----------------------------
    circ3.shape(bpty)
    Lol3 = int(Lol3) + int(Ayden)
    if Lol3 == 1:
      sleep(1.5)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      import burnt
    break
circ3.onclick(aper3)
#Steak 4 -----------------------------------------------
def aper4(x,y):
  circ4.shape(rpty)
  sleep(0.5)
  while True:
    global Lol4
    #raw------------------
    def BENZOS(x,y):
      global Lol4
      Lol4 = int(Lol4) - int(Harrison)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      sleep(0.5)
      import raw
    circ4.onclick(BENZOS)
    sleep(c4)
    circ4.shape(mrpty)
    #Perfect--------------------
    def Nico(x,y):
      global Lol4
      global Ethan
      Lol4 = int(Lol4) - int(Harrison)
      Ethan = int(Ethan) + 1
      circ4.goto(1000,1000)
      while True:
        if Ethan == 4:
          stove.penup()
          stove.speed(0)
          stove.goto(1000,1000)
          import w
          Ethan = int(Ethan) - int(Ethan)
    circ4.onclick(Nico)
    sleep(b4)
    #Burnt----------------------------
    circ4.shape(bpty)
    Lol4 = int(Lol4) + int(Ayden)
    if Lol4 == 1:
      sleep(1.5)
      circ1.goto(1000,1000)
      circ2.goto(1000,1000)
      circ3.goto(1000,1000)
      circ4.goto(1000,1000)
      stove.penup()
      stove.speed(0)
      stove.goto(1000,1000)
      import burnt
    break
circ4.onclick(aper4)

#timer
def tim():
  global Lol1
  global Lol2
  global Lol3
  global Lol4
  Lol1 = int(Lol1) - int(Harrison)
  Lol2 = int(Lol2) - int(Harrison)
  Lol3 = int(Lol3) - int(Harrison)
  Lol4 = int(Lol4) - int(Harrison)
  sleep(10)
  circ1.goto(1000,1000)
  circ2.goto(1000,1000)
  circ3.goto(1000,1000)
  circ4.goto(1000,1000)
  stove.penup()
  stove.speed(0)
  stove.goto(1000,1000)
  import oof
tim()

  








