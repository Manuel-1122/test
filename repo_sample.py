def sum_func(a, b):
    if a or b < 0:
        return abs(a + b)
    else:
        return a + b


print(sum_func(-5, 9))
