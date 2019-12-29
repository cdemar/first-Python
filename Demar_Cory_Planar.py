# Programmer: Cory DeMar
# ComSc 20
# Assognment #6
# Functions Part:2

firstX = int(input("Enter first x: "))
firstY = int(input("Enter first y: "))
secondX = int(input("Enter second x: "))
secondY = int(input("Enter second y: "))

def distance(a, b, c, d):
    x = (a - c) ** 2 + (b - d) ** 2
    y = x ** (1/2)
    return y

def block_distance(a, b, c, d):
    x = abs(a - c) + abs(b - d)
    return x


print ("The Pythagorean distance is", format(distance(firstX, firstY, secondX, secondY), '.2f'))
print ("The city block distance is ", format(block_distance(firstX, firstY, secondX, secondY), '.2f'))
