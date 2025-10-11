#  Find the second largest element in an array

#Solution 1: Complexity: O(n)
def second_largest(arr):
    if len(arr) < 2:
        return None 
    
    first = second = float('-inf')   #Negative infinity value

    for char in arr:
        if char > first:
            second = first     #-inf
            first = char       # 10
        elif char > second and char!= first:
            second = char
    
    return second

#Solution 2: Complexity O(n)
def second_largest_set_max(arr):
    unique = set(arr)

    if len(unique) < 2:
        return None
    
    unique.remove(max(unique))
    return max(unique)


arr = list(map(int, input("Enter array elements space separated: ").split()))
print("Second Largest Element:", second_largest(arr))
# print("Second Largest Element:",second_largest_set_max(arr))  