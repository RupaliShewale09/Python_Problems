# Sum of first n natural numbers

def natural_sum(n):
    if n == 0:
        return 0

    return n + natural_sum(n-1)

num = int(input("Enter a number: "))
print(f"Sum of 1st {num} natural numbers:", natural_sum(num))