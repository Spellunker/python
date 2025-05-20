"""while True:
    print("It`ll take too long")
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint

inputed_number = -1
guess_counter = 0
secret_number = randint(0, 9)

while inputed_number != secret_number:
    inputed_number = int(input("Input a number: "))
    guess_counter += 1

print(f"Secret number {secret_number} was found!")
print(f"It took {guess_counter} try(ies) to be found!")
