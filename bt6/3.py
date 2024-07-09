n = int(input())
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n > 0:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n+2) - fibonacci(n+1)
print(fibonacci(n))