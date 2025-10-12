# Given an array of positive integers and a number X, 
# count the number of contiguous subarrays whose sum is exactly X.

# Enter space separated values: 1 2 3 0 3 1 1 1 2
# Enter sum:3
# Count  of subarrays: 6      --- [1 2] [3] [3 0] [0 3] [3] [1 1 1] [1 2]

def count_subarray(arr, x):
    start = 0
    count = 0
    curr_sum = 0

    for end in range(len(arr)):
        curr_sum += arr[end]

        while curr_sum > x and start <= end:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == x:
            count += 1

    return count

arr = list(map(int, input("Enter space separated values: ").split()))
k = int(input("Enter sum:"))
print("Count of subarrays:", count_subarray(arr, k))
    

