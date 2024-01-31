from functools import cache

@cache
def fibonacci (n):
    if n <= 1:
        return n
    
    else: return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(int(input('Welche Zahl möchten Sie die Fibonacci Zahl: '))))