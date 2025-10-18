# Find Triplets With Sum < K 
#  array : 5 1 3 4 7    K: 12
#  no of triplets : 4


def count_triplets(arr, K):
    arr.sort()    
    count = 0

    for i in range(len(arr) - 2):    
        j = i + 1    
        k = len(arr)-1     

        while j < k:
            current_sum = arr[i] + arr[j] + arr[k]     

            if current_sum < K:
                count += (k - j)   
                j += 1  
            else:
                k -= 1    
    return count


arr = list(map(int, input("Enter array elements: ").split()))
K = int(input("Enter K value: "))
print("Number of triplets with sum <", K, ":", count_triplets(arr, K))
