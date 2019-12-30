#   Programmer: Cory DeMar
#   ComSc 20
#   Final Exam

class Car:
    def __init__(self, year_make, model):
        self.year_model = year_model;
        self.make = make
        self.speed = 0

    def get_speed(self):
        return self.speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -+ 5