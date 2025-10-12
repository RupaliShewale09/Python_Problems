# Given an array arr[] of size n and an integer k, reverse every consecutive k elements of the array.

# arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
# Output: [3, 2, 1, 6, 5, 4, 8, 7]

# Time Complexity : O(n)
def reverse(arr, k):
    for i in range (0, len(arr), k):
        left = i
        right = min(i+k-1, len(arr)-1)

        while left < right:
            arr[left] , arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr = list(map(int, input("Enter space separated values: ").split()))
k = int(input("Enter k:"))
print("array with reversing every consecutive k elements: ", reverse(arr, k))
