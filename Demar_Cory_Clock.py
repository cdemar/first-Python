# Programmer: Cory DeMar
# ComSc 20
# Assognment #5
# Turtle Grouphic/Loops Part Two
# 2-22-17

import turtle
wn = turtle.Screen()
wn.bgcolor("orange")


circle = turtle.Turtle()
circle.pensize(5)
circle.speed(10)
circle.penup()
circle.forward(150)
circle.pendown()
circle.left(90)
circle.circle(150)

clock = turtle.Turtle()
clock.shape("square")
clock.penup()
clock.color("blue")
clock.speed(10)
for size in range(12):
        clock.forward(150)
        clock.stamp()
        clock.forward(-150)
        clock.right(30)

import datetime
hour = datetime.datetime.now().hour % 12
minute = datetime.datetime.now().minute
minAngle = minute * 6 - 90
hrAngle = hour * 30 - 90

hour = turtle.Turtle()
hour.color("red")
hour.pensize(5)

hour.right(hrAngle)
hour.forward(100)

minute = turtle.Turtle()
minute.color("red")
minute.pensize(3)

minute. right(minAngle)
minute.forward(120)

wn.exitonclick()