#turtle setup
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
l1=float(3)
l2=float(0)
t.width(1)
#Dragon
t.color('black', 'green')
t.turtlesize(0.01)
t.speed(100)
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.left(90)
t.forward(50)
t.right(90)
t.forward(25)
t.pendown()
t.color('black', 'white')
t.begin_fill()
t.circle(10)
t.end_fill()
t.color('black', 'black')
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.right(180)
t.forward(50)
t.pendown()
t.color('black', 'white')
t.begin_fill()
t.circle(10)
t.end_fill()
t.color('black', 'black')
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()
t.right(180)
t.forward(75)
t.pendown()
t.color('black', 'green')
t.begin_fill()
t.forward (100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(150)
t.right(180)
t.end_fill()
while l1 > l2:
    t.begin_fill()
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.end_fill()
    l2 += 1
t.begin_fill()
t.left(90)
t.forward(50)
t.right(45)
t.forward(50)
t.right(90)
t.forward(25)
t.right(90)
t.forward(75)
t.right(135)
t.forward(35)
t.end_fill()



#shortcuts

import turtle
from turtle import *
 
setup(500, 500)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
turtle.width(5)
showturtle()
 
 
def up():
    turtle.setheading(90)
    turtle.forward(100)
 
def up():
    turtle.setheading(90)
    turtle.forward(100)
def down():
    turtle.setheading(270)
    turtle.forward(100)
def left():
    turtle.setheading(180)
    turtle.forward(100)
def right():
    turtle.setheading(0)
    turtle.forward(100)
def upp():
    turtle.setheading(90)
    turtle.forward(25)
def downp():
    turtle.setheading(270)
    turtle.forward(25)
def leftp():
    turtle.setheading(180)
    turtle.forward(25)
def rightp():
    turtle.setheading(0)
    turtle.forward(25)
 
def circle():
    t.circle(50)
def circles():
    t.circle(25)

def r():
    turtle.color("red")
def g():
    turtle.color("green")
def b():
    turtle.color("blue")
def z():
    turtle.color("black")
 
 
listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')
onkey(upp, 'w')
onkey(downp, 's')
onkey(leftp, 'a')
onkey(rightp, 'd')
onkey(circle, 'o')
onkey(circles, 'p')
onkey(z, "z")
onkey(r, 'r')
onkey(g, 'g')
onkey(b, 'b')
 
mainloop()