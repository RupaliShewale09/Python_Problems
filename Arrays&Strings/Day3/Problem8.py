# Given an array of integers, find the pair of elements (adjacent or any) whose product is maximum.
# Problem1 Input:  [3, 6, -2, -5, 7, 3] Output: 21   (product of 7 * 3)
# Problem2  Input:  [-10, -20, 5, 2] Output: 200   (product of -10 * -20)

# Problem 1 only adjacent
def product(arr):
    max_pro = float('-inf')

    for i in range(1, len(arr)):
        curr_Pro = arr[i]*arr[i-1]

        if curr_Pro > max_pro :
            max_pro = curr_Pro
            pair = (arr[i-1], arr[i])
        
    return pair, max_pro

#another problem: not necessarily adjacent pairs
def max_product(arr):
    max1 = max2 = float('-inf')  #Two largest numbers
    min1 = min2 = float('inf')   #Two smallest numbers

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    pro1 = max1*max2
    pro2 = min1*min2
    if pro1 > pro2:
        return (max1, max2) , pro1
    else:
        return (min1, min2) , pro2    

arr = list(map(int,input("Enter space separated elements: ").split()))
print("The pair of element(adjucent) with max product:", (product(arr)))
# print("The pair of element(any) with max product:", (max_product(arr)))