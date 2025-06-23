def gcd(numbers):
    lista = sorted(numbers)
    for possible_number in range(lista[0], 0, -1):
        counter = 0
        for number in numbers:
            if number % possible_number != 0:
                break
            else:
                counter += 1

        if counter == len(numbers):
            return f"{possible_number} is the gcd!"


if __name__ == "__main__":
    print(gcd([21, 7]))  # 7
    print(gcd([125, 40]))  # 5
    print(gcd([9, 564, 66, 3]))  # 3
    print(gcd([55, 22]))  # 11
    print(gcd([15, 150]))  # 15
    print(gcd([7, 9]))  # 1
