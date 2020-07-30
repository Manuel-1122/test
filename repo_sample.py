def sum_func(a, b):
    if a and b < 0:
        return abs(a + b)
    else:
        return a + b


print(sum_func(-5, -9))
