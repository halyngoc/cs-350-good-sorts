import numpy
import time
from mergeSort import mergeSort
from mergeSort import printArray

# random sorting
# ---------------------------------
randomTimes = numpy.zeros(100, dtype=float)
for x in range(0, 99):
    array = numpy.random.randint(0, 10000, 10000)
    start = time.clock()
    mergeSort(array)
    total = time.clock() - start
    randomTimes[x] = total
# printArray(randomTimes)


# sorted sorting
# ---------------------------------
sortedTimes = numpy.zeros(100, dtype=float)
for x in range(0, 99):
    array = numpy.random.randint(0, 1000, 10000)
    array = numpy.sort(array)
    start = time.clock()
    mergeSort(array)
    total = time.clock() - start
    sortedTimes[x] = total
# printArray(sortedTimes)


# reverse order sorting
# ---------------------------------
revTimes = numpy.zeros(100, dtype=float)
rev = numpy.random.randint(0, 1000, 10000)
rev = numpy.sort(rev, axis=None)
rev = numpy.flip(rev, 0)
for x in range(0, 99):

    start = time.clock()
    mergeSort(rev)
    total = time.clock() - start
    revTimes[x] = total
# printArray(revTimes)


# random float sorting
# ---------------------------------
randomFloatTimes = numpy.zeros(100, dtype=float)
for x in range(0, 99):
    array = numpy.random.rand(0, 10, 10000000)
    start = time.clock()
    mergeSort(array)
    total = time.clock() - start
    randomFloatTimes[x] = total

# printArray(randomFloatTimes)