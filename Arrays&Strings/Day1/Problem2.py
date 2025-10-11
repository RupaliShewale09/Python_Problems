#  Count all elements greater than X

def greater(arr, x):
    uni = set(arr)
    count = 0
    greate = []
    for num in uni:
        if num > x:
            greate.append(num)
            count += 1

    return count, greate


arr = list(map(int, input("Enter array elements space separated: ").split()))
x = int(input("Enter x:"))


print("Elements greater than x:", greater(arr, x))