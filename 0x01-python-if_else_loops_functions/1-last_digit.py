#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    c = ((-1 * number) % 10) * -1
else:
    c = number % 10
if c > 5:
    print(f"Last digit of {number} is {c} and is greater than 5")
elif c == 0:
    print(f"Last digit of {number} is {c} and is 0")
elif c < 6 and c != 0:
    print(f"Last digit of {number} is {c} and is less than 6 and not 0")
