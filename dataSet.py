import numpy
import time
from mergeSort import mergeSort
from mergeSort import printArray

#random sorting
start = time.clock()
array = numpy.random.randint(0, 1000000, 10000000)
total = time.clock() - start
print("Total seconds to sort", total)
#printArray(array)
#printArray(mergeSort(array))

