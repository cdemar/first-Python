#---------------------------------------------------
# Written by Cory DeMar 2/6/17
# Variables and Calculations (1)
#---------------------------------------------------

item_1 = float(input("Please enter item 1: "))
item_2 = float(input("Please enter item 2: "))
item_3 = float(input("Please enter item 3: "))
item_4 = float(input("Please enter item 4: "))
item_5 = float(input("Please enter item 5: "))
subTotal = item_1 + item_2 + item_3 + item_4 + item_5
tax_amount = subTotal * .07

print()
print("Subtotal $", format(subTotal, '.2f'))
print("Tax: $", format(tax_amount, '.2f'))
print("Total: $", format(subTotal + tax_amount, '.2f'))