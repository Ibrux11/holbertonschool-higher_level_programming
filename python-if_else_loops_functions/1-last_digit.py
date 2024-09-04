#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
trunks =abs(number) % 10
isagi = 1 if number >= 0 else -1
trunks *= isagi
if number > 5:
    print(f"Last digit of {number} is {trunks} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {trunks} and is 0")
elif number < 5:
    print(f"Last digit of {number} is {trunks} and is less than 6 and not 0")
