# STRETCH: implement Linear Search				
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

print(linear_search([1,2,3], 3))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1

    while low < high:
        mid = (high-low)//2
        if target==arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1 # not found

print(binary_search([1,2,3], 2))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    middle = (low+high)//2

    if len(arr) == 0:
        return -1 # array empty

    if arr[middle]==target:
        return middle
    elif target < arr[middle]:
        binary_search_recursive(arr[:middle-1], target, low, middle-1)
    else:
        binary_search_recursive(arr[middle+1:], target, middle+1, high)

    

print(binary_search_recursive([1,2,3,4,5,6,7,8,9], 7, 0, 8))