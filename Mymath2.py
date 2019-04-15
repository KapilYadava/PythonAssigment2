import math


class Sqroot:

    def sqroot(self, num):
        return math.sqrt(num)


class Addition:

    def addition(self, num1, num2):
        return num1 + num2


class Subtraction:

    def subtraction(self, num1, num2):
        return num1 - num2


class Multiplication:

    def multiplication(self, num1, num2):
        return num1 * num2


class Division:

    def division(self, num1, num2):
        return num1 / num2


class Mymath(Sqroot):

    def sqroot(self, num):
        print(str(super(Mymath, self).sqroot(num)))


mymath = Mymath()
mymath.sqroot(3)


class Mymath(Addition):

    def addition(self, num1, num2):
        print(str(super(Mymath, self).addition(num1, num2)))


mymath = Mymath()
mymath.addition(3, 2)


class Mymath(Subtraction):

    def subtraction(self, num1, num2):
        print(str(super(Mymath, self).subtraction(num1, num2)))


mymath = Mymath()
mymath.subtraction(3, 2)


class Mymath(Multiplication):

    def multiplication(self, num1, num2):
        print(str(super(Mymath, self).multiplication(num1, num2)))


mymath = Mymath()
mymath.multiplication(3, 2)


class Mymath(Division):

    def division(self, num1, num2):
        print(str(super(Mymath, self).division(num1, num2)))


mymath = Mymath()
mymath.division(3, 2)
