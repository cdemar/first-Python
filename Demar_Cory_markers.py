# programer: Cory DeMar
# Midterm 1


#input data
markers = int(input("How many markers are you buying? "))

package = markers // 5
marker = markers % 5

packagePrice = package * 3.5
markerPrice = marker * .8
subtotal = packagePrice + markerPrice
shipping = subtotal * .05
tax = subtotal * .065
total = subtotal + shipping + tax


print("Number of packages:", package)
print("Number of seprate markers:", marker)
print("Subtotal: $", format(subtotal, '.2f'))
print("Tax:      $", format(tax, '.2f'))
print("shipping: $", format(shipping, '.2f'))
print("Total:    $", format(total, '.2f'))
