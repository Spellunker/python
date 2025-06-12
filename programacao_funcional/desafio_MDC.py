def gcd(numbers):
    lista = sorted(numbers)
    for possible_number in range(lista[0], 0, -1):
        # Do a loop where it tries the mod % of the possible numbers within the numbers inside the lista
        # If all mods returns 0, then the possible number is the gcd
        # If none of the numbers is the gcd, then the number 1 will be the gcd


if __name__ == "__main__":
    print(gcd([21, 7]))  # 7
    print(gcd([125, 40]))  # 5
    print(gcd([9, 564, 66, 3]))  # 3
    print(gcd([55, 22]))  # 11
    print(gcd([15, 150]))  # 15
    print(gcd([7, 9]))  # 1
