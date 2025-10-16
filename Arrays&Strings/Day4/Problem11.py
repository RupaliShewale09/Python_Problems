# Given an array of integers, rearrange its elements so that all negative numbers appear on the left side 
# and all positive numbers appear on the right side of the array. can rearrange freely. must do this in-place 
# (without using any extra array).
# Input:  [1, -3, 5, -2, -8, 6, -1, 0]    Output: [-3, -2, -8, -1, 1, 5, 6, 0]

def partition(arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        if (arr[left] >= 0) and (arr[right] < 0):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif (arr[left] >= 0) and (arr[right] >= 0) :
            right -= 1
        elif arr[left] < 0 and arr[right] < 0 :
            left += 1
        else:
            left +=1
            right -=1

    return arr

arr = list(map(int, input("Enter space separated values: ").split()))
print("The new partitioned array: ",partition(arr))