import turtle
import time
cr = turtle.Turtle()
burnt = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("grey")
sleep = time.sleep

bpty = "burnt.jpg"

screen.addshape(bpty)
burnt.penup()
burnt.speed(0)
burnt.shape(bpty)
burnt.left(90)
burnt.goto(0,100)

cr.hideturtle()
cr.speed(0)
cr.penup()
cr.goto(-150,0)
cr.color("white")
cr.write("GAME OVER", "center", font=("copperplate", 40, "normal"))
cr.goto(-310,-30)
cr.write("JEEZ THAT THING ISN'T EVEN A COW ANYMORE!", "center", font=("copperplate", 20, "normal"))
sleep(1.5)
cr.goto(-230,-60)
cr.write("Pay attention to when the steak is done goofy.", "center", font=("copperplate", 20, "normal"))
cr.goto(-50, -90)
cr.write("Refresh Page to replay.", "center", font=("copperplate", 15, "normal"))