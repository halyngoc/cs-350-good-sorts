# Python implementation of MergeSort
import numpy


def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def insertionSort(array):

    # Sort each element
    for i in range(1, len(array)):

        key = array[i]

        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return


def mergeSortHybrid(array):
    # check to see if array needs to split
    # count = array.size
    tempArray = numpy.copy(array)
    # tempArray[:] = array

    if len(array) > 10:

        # split array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        # printArray(left)
        # printArray(right)

        right = mergeSortHybrid(right)  # sort right half
        left = mergeSortHybrid(left)  # sort left half
        x = 0
        y = 0
        z = 0

        # recursive calls have finished, sort left and right and merge to tempArray

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                tempArray[z] = left[x]
                x += 1
            else:
                tempArray[z] = right[y]
                y += 1
            z += 1

        # check for remaining elements in both sub arrays
        while x < len(left):
            tempArray[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            tempArray[z] = right[y]
            y += 1
            z += 1
    else:
        insertionSort(tempArray)
    return tempArray


# array2 = numpy.array([1, 7, 324, 45, 83, 33, 25, 37, 4, 80, 4567, 1, 57, 2, 5, 14, 11, 10])
# printArray(array2)
# array2 = mergeSortHybrid(array2)
# printArray(array2)

