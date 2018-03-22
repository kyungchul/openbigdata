def fib(n):
    array = [0, 1]
    i = 0
    while array[i] + array[i+1] < n:
        array.append(array[i]+array[i+1])
        i += 1
    return array

result = fib(13)
print(result)
