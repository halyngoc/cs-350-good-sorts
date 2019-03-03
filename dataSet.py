import numpy
import time
from mergeSort import mergeSort
from mergeSort import printArray

#random sorting

randomTimes = numpy.zeros(100, dtype=float)
for x in range(0, 99):
    array = numpy.random.randint(0, 10000, 10000)
    start = time.clock()
    mergeSort(array)
    total = time.clock() - start
    randomTimes[x] = total





printArray(randomTimes)

#printArray(array)
#printArray(mergeSort(array))

#sorted sorting
array = numpy.random.randint(0, 1000, 100000)
array = numpy.sort(array)
start = time.clock()
mergeSort(array)
total = time.clock() - start
print("Total seconds to sort", total)


#reverse order sorting
start = time.clock()
#array2 = numpy.random_sample(0, 1000000, 10000000)
total = time.clock() - start

#compare floats

