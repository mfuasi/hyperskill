def range_sum(numbers, start, end):
    return sum(filter(lambda x: start <= x <= end, numbers))


input_numbers = map(int, input().split())
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))
