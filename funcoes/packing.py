#!/usr/bin/python3
def sum_2(a, b):
    return a + b


def sum_3(a, b, c):
    return a + b + c


def sum_n(*numbers):
    starter_sum = 0
    for n in numbers:
        starter_sum += n
    return starter_sum


if __name__ == "__main__":
    print(sum_2(2, 3))
    print(sum_3(2, 4, 6))
    
    # packing
    print(sum_n(1))
    print(sum_n(1, 1))
    print(sum_n(1, 1, 1, 1, 1, 1, 1))
    
    # unpacking
    tuple_nums = (1, 2, 3)
    print(sum_3(*tuple_nums))
    list_nums = [1, 2, 3]
    print(sum_3(*list_nums))
