# Name: E. Barton
# Title: lesson 16
# Date: March 24, 2025
# Description: This program finds the average of 100

import random


position = 0

def sum (numbers):
    add = 0
    for i in range (100):
        add = add + numbers[i]
    result = add
    return result

def average (numbers):
    result = sum(numbers) / 100
    return result

numbers = []
for i in range (100):
    num = random.randint(1,100)
    numbers.append(num)

print(numbers[1:99])
print("Therefore the average of all numbers is " ,average(numbers))

