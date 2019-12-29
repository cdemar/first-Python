# Programmer: Cory DeMar
# ComSc 20
# Assognment #8
# Software Sales Part 2

price = float(input("What is the price of each item? $ "))
batch = int(input("How many are you ordering? "))

def discount(batch):
    if (batch > 100):
        return .30
    elif(batch > 50):
        return .25
    elif(batch > 20):
        return .20
    elif(batch > 10):
        return .10
    else:
        return .0

subtotal = price * batch
discountAmount = subtotal * discount(batch)
total = subtotal - discountAmount

print("Subtotal: $ ", format(subtotal, '.2f'))
print("Discount: $ ", format(discountAmount, '.2f'))
print("Total:    $ ", format(total, '.2f'))