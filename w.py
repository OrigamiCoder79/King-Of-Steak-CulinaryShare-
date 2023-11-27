import turtle
import time
cr = turtle.Turtle()
screen = turtle.Screen()
sleep = time.sleep
#text
def text():
  cr.hideturtle()
  cr.speed(0)
  cr.penup()
  cr.goto(-150,0)
  cr.color("Black")
  cr.write("Good Job!", "center", font=("copperplate", 40, "normal"))
  cr.goto(-140,-30)
  cr.write("Amazing cooking", "center", font=("copperplate", 20, "normal"))
  sleep(0.5)
  cr.goto(-160,-60)
  cr.write("How did you even find this...it's suposed to be secret...", "center", font=("copperplate", 10, "normal"))
text()

#color changing backgorund
while True:
  screen.bgcolor("blue")
  sleep(0.5)
  screen.bgcolor("yellow")
  sleep(0.5)
  screen.bgcolor("orange")
  sleep(0.5)
  screen.bgcolor("red")
  sleep(0.5)
  screen.bgcolor("pink")
  sleep(0.5)
  screen.bgcolor("purple")
  sleep(0.5)
  screen.bgcolor("grey")
  cr.clear()
  sleep(0.2)
  import credits
  break
  