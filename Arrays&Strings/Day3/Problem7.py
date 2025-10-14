# Given an array of integers, find the length and elements of the longest contiguous subarray 
# where all elements are in strictly increasing order.
# Input:  [1, 2, 2, 4, 5, 7, 3]
# Output:  [2, 4, 5, 7] 4

def contiguous_arr(arr):
    start = 0
    curr_start = 0
    max_len = 1
    curr_len = 1

    for i in range (1, len(arr)):
        if arr[i] > arr[i-1]:
            curr_len+=1
        else:
            if curr_len > max_len:
                max_len = curr_len
                start = curr_start
            curr_len = 1
            curr_start = i

    if curr_len > max_len:   #for last 
        max_len = curr_len
        start = curr_start

    return arr[start : start + max_len], max_len
 

arr = list(map(int, input("Enter space separated values: ").split()))
print("Count of subarrays:", contiguous_arr(arr))