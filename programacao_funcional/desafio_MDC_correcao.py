def gcd(numbers):
    def calc(divider):
        return divider if sum(map(lambda x: x % divider, numbers)) == 0 \
            else calc(divider - 1)
    return calc(min(numbers))


if __name__ == "__main__":
    print(gcd([21, 7]))  # 7
    print(gcd([125, 40]))  # 5
    print(gcd([9, 564, 66, 3]))  # 3
    print(gcd([55, 22]))  # 11
    print(gcd([15, 150]))  # 15
    print(gcd([7, 9]))  # 1
