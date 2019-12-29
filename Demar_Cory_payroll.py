# Programmer: Cory DeMar
# ComSc 20
# Assognment #7
# Payroll Part 1

hrs = int(input("How mant hour worked this week: "))
wage = float(input("What is your hourly wage: $ "))

def wages(hrs, wage):
    if  hrs <= 40:
        result = hrs * wage
    else:
        dif = hrs - 40
        rate = wage * 1.5
        result = 40 * wage + (dif * rate)
    return result

print("This is the amount you will earn this week $",
      format(wages(hrs, wage), '.2f'))