import numpy
import time
from mergeSort import mergeSort
from mergeSort import printArray
from mergeHybrid import mergeSortHybrid
from mergeHybrid import insertionSort
from Quicksort import quicksort
from heapsort import sort


# random sorting
# ---------------------------------
# randomTimes = numpy.zeros(100, dtype=float)
# for x in range(0, 100):
#    array = numpy.random.randint(0, 10000, 10000)
#    start = time.perf_counter()
#    sort(array)
#    total = time.perf_counter() - start
#    randomTimes[x] = total
# printArray(randomTimes)
# print("Mean time for random sorts: ", numpy.mean(randomTimes))



# sorted sorting
# ---------------------------------
# sortedTimes = numpy.zeros(100, dtype=float)
# for x in range(0, 99):
#    array = numpy.random.randint(0, 1000, 10000)
#   array = numpy.sort(array)
#   start = time.perf_counter()
#   mergeSort(array)
#   total = time.perf_counter() - start
#   sortedTimes[x] = total
# printArray(sortedTimes)


# reverse order sorting
# ---------------------------------
revTimes = numpy.zeros(1000, dtype=float)
for x in range(0, 1000):
    rev = numpy.random.randint(0, 1000, 1000)
    rev = numpy.sort(rev, axis=None)
    rev = numpy.flip(rev, 0)
    start = time.perf_counter()
    insertionSort(rev)
    total = time.perf_counter() - start
    revTimes[x] = total
# printArray(revTimes)
print("Mean for reverse order heap (s): ", numpy.mean(revTimes))




# random float sorting
# ---------------------------------
# randomFloatTimes = numpy.zeros(100, dtype=float)
# for x in range(0, 99):
#    array = numpy.random.rand(0, 10, 10000000)
#    start = time.perf_counter()
#    mergeSort(array)
#    total = time.perf_counter() - start
#    randomFloatTimes[x] = total

# printArray(randomFloatTimes)

# Merge-sort worst case
# ---------------------------------------
# badTimes = numpy.zeros(100, dtype=float)
