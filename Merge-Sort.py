# Python implementation of MergeSort

def mergeSort(array):
    # check to see if array needs to split
    if len(array) > 1:

        # split array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left) # sort left half
        mergeSort(right) # sort right half

        x = 0
        y = 0
        z = 0

        # recursive calls have finished, sort left and right and merge to array

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                array[z] = left[x]
                x += 1
            else:
                array[z] = right[y]
                y += 1
            z += 1

        # check for remaining elements in both sub arrays

        while x < len(left):
            array[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            array[z] = right[y]
            y += 1
            z += 1


def printArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Main function

array = [43, 45, 765, 23, 77, 9, 23, 5, 2]

printArray(array)

mergeSort(array)

printArray(array)