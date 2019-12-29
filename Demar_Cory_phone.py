# Programmer: Cory DeMar
# ComSc 20
# Assognment #9
# Phone Plan Part 3

# Does this work
def get_units():
    valid_input = False
    while not valid_input:
        units = int(input("Enter number of units used: "))
        if units >= 0:
            valid_input = True 
        else:
            print("You cannot have negative units.")
    return units

# The math Part
def calculate_cost(units, basePlan, baseLimit, planOver):
    if units <= baseLimit:
        return basePlan
    else:
        numAmmount = units - baseLimit
        placement = basePlan + (numAmmount * planOver)
        return placement

units = get_units()

# Simple looking
planOne = calculate_cost(units, 9.38, 65, .045)
planTwo = calculate_cost(units, 8.57, 50, .052)

# The output
print("Cost for plan 1: $", format(planOne, '.2f'))
print("Cost for plan 2: $", format(planTwo, '.2f'))

# Plan that is Cheaper
if planOne < planTwo:
    print("Plan 1 is cheaper.")
else:
    print("Plan 2 is cheaper.")