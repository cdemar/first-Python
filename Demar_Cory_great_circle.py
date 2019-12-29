# Programmer: Cory DeMar
# ComSc 20
# Assognment #6
# Functions Part:3
# 3-13-17

import math

from math import sin, cos, tan, acos, asin, radians

def great_circle_distance (a, b, c, d):
    a = radians(a)
    b = radians(b)
    c = radians(c)
    d = radians(d)

    r = 6371
    x = sin (a) * sin (c)
    y = cos(a) * cos(c) * cos(abs (b - d))
    z = acos(x + y)
    d = r * z
    return d

def km_to_miles (a):
    x = a * .621371
    return x

d1 = great_circle_distance(37.33, -121.9, 41.83, -87.68)
d2 = great_circle_distance(41.83, -87.68, 38.9, -77.02)

print("Distance from San Jose to Chicago is", int(d1) ,"km or", int(km_to_miles(d1)) , "miles.")
print("Distance from Chicago to Washington D.C. is", int(d2) , "km or", int(km_to_miles(d2)) , "miles.")