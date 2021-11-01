import random
import sys
import time
from random import randint

from ComplexNumber import ComplexNumber
from Coordinates import Coordinates
from Fraction import Fraction


def printToConsole(numbers, inpfile):
    print('given input file:\n'
          '---------------------------')
    print(inpfile.read())
    print('---------------------------')

    for n in numbers:
        print(n.toString())


def printToFile(numbers, inpfile, outfile):
    outfile.write('given input file:\n'
                  '---------------------------\n')
    outfile.write(inpfile.read())
    outfile.write('\n---------------------------\n')

    for n in numbers:
        outfile.write(n.toString() + '\n')

def bubbleSort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j].convertToReal() > numbers[j + 1].convertToReal():
                help = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = help
    return numbers


starttime = time.time()
numbers = list()
if len(sys.argv) == 1:
    print("Run main <input.txt> to specify input file \n"
          "or\n"
          "run main <input.txt> <output.txt> to specify"
          "input file, output will be written into output.txt\n"
          "or\n"
          "run main -generate <amount> <lowerbound> <upperbound> <out.txt> to generate "
          "a text file with tests\n")
    exit(0)

if (sys.argv[1] == '-generate'):
    genfile = open(sys.argv[5])
    for i in range(0, int(sys.argv[2])):
        genfile.write(str(randint(0, 3)) + str(random.uniform(float(sys.argv[3]), float(sys.argv[4])))
                      + str(random.uniform(float(sys.argv[3]), float(sys.argv[4]))))
    genfile.close()
    exit(0)

inpfile = open(sys.argv[1])
errorsOccured = False
errorsFile = open('errors.log', 'w+')
lineNumber = 0
for line in inpfile.readlines():
    lineNumber += 1
    typestr, firststr, secondstr = line.split()
    type = int(typestr)
    first = float(firststr)
    second = float(secondstr)
    if type == 0:
        numbers.append(ComplexNumber(first, second))
    elif type == 1:
        if second == 0:
            errorsOccured = True
            errorsFile.write('Denominator equals to zero (line ' + str(lineNumber) + ')')
        else:
            numbers.append(Fraction(first, second))
    else:
        numbers.append(Coordinates(first, second))
inpfile.seek(0)
numbers = bubbleSort(numbers)
# print(' '.join(map(lambda x: x.toString(), numbers)))
finishitime = time.time()
print('program execution finished in ' + str(finishitime - starttime) + ' s.')

if len(sys.argv) == 2:
    printToConsole(numbers, inpfile)
else:
    outfile = open(sys.argv[2], 'w+')
    printToFile(numbers, inpfile, outfile)
    outfile.close()

inpfile.close()
