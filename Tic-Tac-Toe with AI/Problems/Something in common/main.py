def calculate_linear(k, b, x):
    y = k * x + b
    common_part(y)


def calculate_quadratic(a, b, c, x):
    y = (a * x * x) + (b * x) + c
    common_part(y)


# create function common_part
def common_part(val):
    print(f'Value of the function equals {val}')
    return val
