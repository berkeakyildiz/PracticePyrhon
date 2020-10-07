import numpy
from random import randint

size1 = randint(0, 100)
size2 = randint(0, 100)

array1 = numpy.random.randint(low=0, high=1000, size=size1)
array1.sort()
array2 = numpy.random.randint(low=0, high=1000, size=size2)
array2.sort()

solArray = []

print(array1)
print(array2)

for i in array1:
    if(i in array2):
        if(i not in solArray):
            solArray.append(i)

print(solArray)