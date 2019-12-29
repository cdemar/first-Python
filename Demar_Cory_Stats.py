# Programmer: Cory DeMar
# ComSc 20
# Assognment #6
# Functions Part:1
# 3-13-17

def reciprocal(a):
    x = 1 / a
    return x

def mean(a, b, c):
    x = a + b + c
    y = x / 3
    return y

def geometric_mean(a, b, c):
    x = a * b * c
    y = x ** (1 / 3)
    return y

def harmonic_mean(a, b, c):
    x = (1 / a) + (1 / b) + (1 / c)
    y = 3 / x
    return y

def main():
    print("Reciprocal of 8 is", format reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")
    
    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")
    
    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
          "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
          "[should be 8.3.999...]")
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
          "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
          "[should be 2.0]")
main()