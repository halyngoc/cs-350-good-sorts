# Python implementation of MergeSort
import numpy


def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

def insertionSort(array):
    

def mergeSort(array):
    # check to see if array needs to split
    #count = array.size
    tempArray = numpy.copy(array)
    #tempArray[:] = array

    if len(array) > 1:

        # split array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        #printArray(left)
        #printArray(right)


        right = mergeSort(right) # sort right half
        left = mergeSort(left)  # sort left half
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
    return tempArray




# Main function

#array = [43, 45, 765, 23, 2314, 8729, 12383, 77, 9, 23, 5, 2]
#array2 = numpy.array([1, 7, 2, 5, 14, 11, 10])
#printArray(array2)

#mergeSort(array)


#printArray(mergeSort(array2))
#printArray(array)



