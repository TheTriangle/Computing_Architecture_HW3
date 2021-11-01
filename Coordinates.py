class Coordinates:
    angle = 0.0
    value = 0.0

    def __init__(self, first, second):
        self.angle = first
        self.value = second

    def convertToReal(self):
        return self.value

    def toString(self):
        return 'Coordinates (' + str(self.angle) + '; ' + str(self.value) + ') - ' + str(self.convertToReal())