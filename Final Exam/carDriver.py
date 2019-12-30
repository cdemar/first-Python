#   Programmer: Cory DeMar
#   ComSc 20
#   Final Exam


import car

def main():
    #create an insurance car
    my_car = car.Car('2008', 'Handa Accord')
    
    # accelerates 5x
    print('car is accelerating: ')
    for i in range(5):
        my_car.accelerate()
        print ('current speed: ' + my_car.get_speed())
    print()
    
    #brakes 5x
    print('car is braking: ')
    for i in range(5):
        my_car.brake()
        print ('current speed: ' + my_car.get_speed())

main()

