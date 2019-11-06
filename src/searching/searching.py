# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (high+low)//2
        if target==arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    middle = (low+high)//2
    #base cases
    if len(arr)==0:
        return -1
    if arr[middle]==target:
        return middle
    if high==low:
        return -1 # array empty

    if target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle-1)
    else:
        return binary_search_recursive(arr, target, middle+1, high)