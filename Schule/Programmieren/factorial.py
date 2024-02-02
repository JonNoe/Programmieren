def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
    
def faktorisieren(fak):
    if (fak == 1):
        return 1
    else:
        return fak * faktorisieren(fak-1)
result = factorial(2)
print(result)




defaultdict = __import__('collections').defaultdict
count = defaultdict(int) #hash table, keys are everything
cache = {}
def fibonacci(n):
    #count[n] += 1 nicht mehr nötig
    if n in cache:
        print(f'cache used for n = {n}')
        return cache[0]
    elif n == 0:
        cache[0] = 0
        return 0
    elif n == 1:
        cache[1] = 1
        return 1
    else:
        result1 = fibonacci(n-1)
        result2 = fibonacci(n-2)
        
        cache[n] = result1 + result2
        result = result1 +result2
    return result

n = int(input('Number: '))
print(f'Die Ergebnis ist {fibonacci(n)}')
for key in count:
    print('fibonacci of', key, 'is called ', count[key], ' times')


        