# Programmer: Cory DeMar
# ComSc 20
# Midturn 2
# Program for Circle and Rectangle

import math

from math import pi
# This is for the Circle Area
def circle_area(radius):
    a = radius * pi
    answer = print("The area of the circle is", format(a, '.2f'))
    return answer
# This is for the Circle circumference
def circle_circumference(radius):
    a = (2 * pi) * radius
    answer = print("The circumference of the circle is", format(a, '.2f'))
    return answer
# This is for the rectangle area
def rectangle_area(length, width):
    a = length * width
    answer = print("The area of the circle is", format(a, '.2f'))
    return answer
# This is for the rectangle perimeter
def rectangle_perimeter(length, width):
    a = (2 * length) + (2 * width)
    answer = print("The perimeter of the circle is", format(a, '.2f'))
    return answer
# This is what the user sees
def display_memu():
    print("   MENU")
    print("1) Area of circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")
    #This allows the computer to know if the number they wrote was acurate or not
    answer = False
    while not answer:
        choice = input("Enter the number you want: ")
        if choice in '12345':
            answer = True
        else:
            print("Enter the number not the word")
    return choice
# This is what the computer is thinking about when the user gives the information
def main():
    choice = display_memu()
    while choice != '5':
        if choice == '1':
            radius = float(input("Enter the circle radius: "))
            cArea = circle_area(radius)
        elif choice == '2':
            radius = float(input("Enter the circle radius: "))
            cCircum = circle_circumference(radius)
        elif choice == '3':
            length = float(input("Enter the rectangle length: "))
            width = float(input("Enter the rectangle width: "))
            rArea= rectangle_area(length, width)
        elif choice == '4':
            length = float(input("Enter the rectangle length: "))
            width = float(input("Enter the rectangle width: "))
            rPerim = rectangle_perimeter(length, width)
        choice = display_memu() 

    print("Thank you and have a nice day")
    
main() 