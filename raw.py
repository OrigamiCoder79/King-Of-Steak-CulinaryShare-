import turtle
import time
cr = turtle.Turtle()
screen = turtle.Screen()
ben = turtle.Turtle()
screen.bgcolor("grey")
sleep = time.sleep

rpty = "rpty.jpg"
screen.addshape(rpty)

ben.speed(0)
ben.penup()
ben.left(90)
ben.goto(0, 100)
ben.shape(rpty)

cr.hideturtle()
cr.speed(0)
cr.penup()
cr.goto(-150,0)
cr.color("white")
cr.write("GAME OVER", "center", font=("copperplate", 40, "normal"))
cr.goto(-170,-30)
cr.write("Why did the cow cross the road?", "center", font=("copperplate", 20, "normal"))
sleep(1.5)
cr.goto(-180,-60)
cr.write("BECAUSE YOU DIDN'T COOK IT", "center", font=("copperplate", 20, "normal"))
cr.goto(-50, -90)
cr.write("Refresh Page to replay.", "center", font=("copperplate", 15, "normal"))
exit()
