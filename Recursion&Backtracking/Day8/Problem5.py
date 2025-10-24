# Fibonacci num

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

num = int(input("Enter a number: "))
print(f"Fibonacci {num}:", fib(num))

