# Find all pairs whose sum = k 

# Solution 1: O(n^2)
def find_pairs(arr, k):
    pairs = set()

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                pairs.add((arr[i],arr[j]))
    return pairs

# solution 2: O(n)
def find_pairs_optimized(arr, k):
    seen = set()
    pairs = set()

    for char in arr:
        target = k - char
        if target in seen:
            pairs.add((target, char))
        seen.add(char)

    return pairs

arr = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter sum value k: "))
print("Pairs with sum", k, ":", find_pairs(arr, k))
print("Pairs with sum", k, ":", find_pairs_optimized(arr, k))