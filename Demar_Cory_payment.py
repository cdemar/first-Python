# Programmer: Cory DeMar
# ComSc 20
# Assognment #2
# Variables and Calculations (2) - Part One
# 2-13-17

principal = float(input("Enter amount of loan: $"))
interest = float(input("Enter annual interest rate as a percent: "))
number_years = float(input("Enter number of years for the loan: "))


monthly_rate = interest / 1200
months = number_years * 12
subformula = (1 + monthly_rate) ** months
payment = principal * (monthly_rate * subformula) / (subformula - 1)

print()
print("Your monthly payment is $", format(payment, '.2f'))