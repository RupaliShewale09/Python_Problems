# Given an array of integers arr[] of size n, find the maximum sum among all contiguous subarrays
# that have a size of k

# ex: [1, 3, 4, 2, 1, 3]   k=3
# [1, 3, 4] => 8      [3, 4, 2] => 9     [4, 2, 1] => 7     [2, 1, 3] => 6      max=9

# SLIDING WINDOW
def max_sum(arr, k):
    window_sum = sum(arr[:k])
    maxSum = window_sum
    max_start = 0
    for i in range (k, len(arr)):
        window_sum += arr[i] - arr[i-k]     # add next and subtract prev from window

        if window_sum > maxSum:
            maxSum = window_sum
            max_start = i - k + 1

    max_window = arr[max_start : max_start+k]
    return maxSum, max_window

arr = list(map(int, input("Enter space separated values: ").split()))
k = int(input("Enter k:"))
print("Maximum Sum ans Subarray:", max_sum(arr, k))