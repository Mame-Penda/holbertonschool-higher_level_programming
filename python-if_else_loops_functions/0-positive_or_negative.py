#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive".format)
elif number == 0:
    print(f"{number} is zero".format)
else:
    print(f" {number} is negative".format)
