def main():
    number_list = []

    low = 0.0
    high = 0.0
    total = 0.0
    average = 0.0
    number = 0

    for i in range(10):
        number = float(input('enter number ' + str(i+1) + ' of 10: '))
        number_list.append(number)

    low = min(number_list)
    high = max(number_list)
    total = sum(number_list)
    avrage = total / 10.0

    print('low', low)
    print('high', high)
    print('total', format(total, ',.2f'))
    print('avrage', format(total, ',.2f'))

main()