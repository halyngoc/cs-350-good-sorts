import numpy
import math

#swap arr[i] and arr[j]
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def get_parent_index(i):
    return math.floor((i - 1) / 2)

def get_left_child_index(i):
    return 2 * i + 1

def get_right_child_index(i):
    return 2 * i + 2

    
def sift_down(arr, start, end):
    root = start

    # while root has at least one child
    while get_left_child_index(root) <= end:
        child = get_left_child_index(root)
        child_to_swap = root

        if arr[child_to_swap] < arr[child]:
            child_to_swap = child

        if child + 1 <= end and arr[child_to_swap] < arr[child + 1]:
            child_to_swap = child + 1

        if child_to_swap == root:
            return
        else:
            swap(arr, root, child_to_swap)
            root = child_to_swap

    
def build_max_heap(arr, count):
    start = get_parent_index(count - 1)

    while start >= 0:
        sift_down(arr, start, count - 1)
        start -= 1
    
def sort(arr):
    count = arr.size
    arr_copy = numpy.empty(count)
    arr_copy[:] = arr

    build_max_heap(arr_copy, count)

    end = count - 1

    while end > 0:
        swap(arr_copy, end, 0)
        end -= 1
        sift_down(arr_copy, 0, end)

    return arr_copy
