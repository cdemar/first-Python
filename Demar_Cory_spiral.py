# Programmer: Cory DeMar
# ComSc 20
# Assognment #4
# Turtle Grouphic/Loops Part One
# 2-22-17

import turtle

side = int(input("How many sides: "))
spirals = int(input("How many spirals: "))
pctGrowth = float(input("What lanth, as percentage, do you want: "))
pct = pctGrowth / 100

wn = turtle.Screen()
wn.bgcolor ("black")
bethel = turtle.Turtle()

bethel.color("red")
bethel.pensize(1)
length = 10
    
for x in range (spirals * side):
    bethel.forward(length)
    bethel.left(360 / side)
    length += length*pct

wn.exitonclick()