class Fraction:
    numenator = 0.0
    denominator = 0.0

    def __init__(self, first, second):
        self.numenator = first
        self.denominator = second

    def convertToReal(self):
        return self.numenator/self.denominator

    def toString(self):
        return 'Fraction ' + str(self.numenator) + '/' + str(self.denominator) + ' - ' + str(self.convertToReal())