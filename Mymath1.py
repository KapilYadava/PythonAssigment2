from Mathnew import Arithmetic


class Mymath:

    def __init__(self):
        self.num1 = 3
        self.num2 = 2

    def sqroot(self):
        print("Sqroot: " + str(Arithmetic.sqroot(self.num1)))

    def addition(self):
        print("Addition: " + str(Arithmetic.addition(self.num1, self.num2)))

    def subtraction(self):
        print("Subtraction: " + str(Arithmetic.subtraction(self.num1, self.num2)))

    def multiplication(self):
        print("Multiply: " + str(Arithmetic.multiplication(self.num1, self.num2)))

    def division(self):
        print("Division: " + str(Arithmetic.division(self.num1, self.num2)))


mymath = Mymath()
mymath.sqroot()
mymath.addition()
mymath.subtraction()
mymath.multiplication()
mymath.division()
