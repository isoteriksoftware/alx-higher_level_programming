#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number, "is", "negative" if number < 0 else "positive")