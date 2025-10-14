# find all pairs with sum = k in sorted array


def pairs(arr, k):
    left = 0
    right = len(arr)-1
    count = 0
    pairs = []

    while left < right:
        if arr[left] + arr[right] == k:
            pairs.append((arr[left], arr[right]))
            count += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] < k: 
            left += 1
        else:
            right -= 1 

    return count, pairs

arr = list(map(int, input("Enter space separated values:").split()))
k = int(input("Enter Sum: "))
print("Pairs are: ", pairs(arr, k))