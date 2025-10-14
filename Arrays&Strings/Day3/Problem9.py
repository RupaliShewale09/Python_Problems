# given an array rotate its elements either to the left or right by a k number of positions
# Input:  [1, 2, 3, 4, 5], k = 2 , Left  =>  Output: [3, 4, 5, 1, 2]
# Input:  [1, 2, 3, 4, 5], k = 2 , Right  =>  Output: [4, 5, 1, 2, 3]

def Rotate(arr, k, r):
    k = k % len(arr)

    if r == 'L' or r == 'l':
        return arr[k:] + arr[:k]
    elif r == 'R' or r == 'r':
        return arr[-k:] + arr[:-k]
    
arr = list(map(int, input("Enter space separated values:").split()))
k = int(input("Number of Positions to rotate: "))
r = input("Which side?(L or R): ")

print("New Array: ", Rotate(arr, k, r))