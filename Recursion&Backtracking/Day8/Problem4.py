# Power of a number
# x = 2  n = 5   power = 32

def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

x = int(input("Enter x: "))
n = int(input("Enter n: "))
print(f"{n}th power of {x}:",power(x,n))
