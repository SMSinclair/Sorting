# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    while(len(arrA) > 0 and len(arrB) > 0):
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    
    while len(arrA) > 0:
        merged_arr.append(arrA.pop(0))

    while len(arrB) > 0:
        merged_arr.append(arrB.pop(0))

    return merged_arr

print(merge([], [2,4,6]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    
    left = []
    right = []
    for i in range(0, len(arr)):
        if i < len(arr)/2:
            left.append(arr[i])
        else:
            right.append(arr[i])

    print(f"left: {left}")
    print(f"right: {right}")

    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([9,8,7,6,5,4,3,2,1]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib(n-1) + fib(n-2)