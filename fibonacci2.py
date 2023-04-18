def fibonacci_iterative(num):
    if num <= 1:
        return num
    else:
        a, b = 0, 1
        for i in range(num - 1):
            a, b = b, a + b
        return b

