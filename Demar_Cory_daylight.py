# Programmer: Cory DeMar
# ComSc 20
# Assognment #2
# Variables and Calculations (2) - Part Two
# 2-13-17

import math
latitude  = float(input("Enter latitude in degrees: "))
day = float(input("Enter day of year (1-365): "))

from math import sin, cos, tan, acos, asin, atan, radians, pi

rad = latitude * math.pi / 180
p = asin (0.39795 * cos (0.2163108+2 * atan (0.9671396 * tan (0.00860 * (day - 186)))))
d = 24 - 7.63944 * acos ((sin (0.01454) + sin(rad) * sin(p))/ (cos (rad) * cos (p)))
min = d * 60

print ("There are about", format (min, '.3f'), "minutes of daylight.")