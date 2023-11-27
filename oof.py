import time
import turtle
import sys

sleep = time.sleep
screen = turtle.Screen()
t = turtle.Turtle()

screen.bgcolor("grey")
t.penup()
t.hideturtle()
t.goto(-100,0)
t.write("Game Over", "center", font=("Consolas", 40, "normal"))
sleep(0.5)
t.goto(-250,-30)
t.write("Did I forget to tell you that you have only 10 seconds? ... my bad.", "center", font=("Consolas", 15, "normal"))
t.goto(-100,-50)
t.write("Refresh to play again", "center", font=("Consolas", 15, "normal"))


