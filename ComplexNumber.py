from math import sqrt


class ComplexNumber:
    real = 0.0
    imaginary = 0.0

    def __init__(self, first, second):
        self.real = first
        self.imaginary = second

    def convertToReal(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def toString(self):
        return 'Complex number (' + str(self.real) + '; ' + str(self.imaginary) + ') - ' + str(self.convertToReal())
