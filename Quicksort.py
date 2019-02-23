import random

list = [7,8,2,5,46,89,2,3,7,0,1,46,754,7,22,56,38,94,7,4,8]

def quicksort(A,start,end):

    if(start < end):
        #print("getting pivot")
        pivot = getPivot(A,start,end)
        #print(*A, sep=", ")
        #print("sorting left")
        quicksort(A,start,pivot)
        #print(*A, sep=", ")
        #print("sorting right")
        quicksort(A,pivot + 1, end)
        #print(*A, sep=", ")



def partition(A,start,end):
    #print("partitioning")
    pivot = A[start]
    i = start
    j = end

    print(pivot)
    print(start)
    print(end)
    print(*A, sep=", ")

    while(True):

        while(A[i] < pivot):
            i = i + 1

        while (A[j] >= pivot and j > start):
            j = j - 1

        if(i >= j):
            return j

        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp



def getPivot(A,start,end):
    #print("randomizing pivot")
    num = random.randint(start,end)
    temp = A[start]
    A[start] = A[num]
    A[num] = temp
    return partition(A,start,end)

quicksort(list,0,len(list) - 1)

print(*list, sep=", ")