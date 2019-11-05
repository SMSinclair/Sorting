# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped=True
    while(swapped==True):
        swapped=False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[i+1] = temp
                # note that a swap occured
                swapped = True
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # count array
    #count = [0 for _ in range(maximum+1)]
    count = []
    for x in arr:
        if x >= 0:
            if x > maximum: # add zeros to count to accomodate max
                maximum = x
                count += [0] * ((maximum+1)-len(count))
            count[x] += 1 # increment count at proper index
        else: 
            return "Error, negative numbers not allowed in Count Sort"

    # sumCount array
    total = 0
    for i in range(0, len(count)):
        count[i] = count[i] + total
        total=count[i]
    count.insert(0,0) # slide to the right
    count.pop()

     # create sorted array
    sorted_arr = [0 for _ in range(len(arr))]
    print(sorted_arr)

    for x in reversed(arr): # reverse to maintain stability
        sorted_arr[count[x]] = x
        count[x] -= 1

    return sorted_arr

#print(count_sort([4,3,2,1]))
