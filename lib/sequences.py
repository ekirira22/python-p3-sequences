#!/usr/bin/env python3
import ipdb
# ALGORITHM
# 1. Insert the first two elements which is 0 and 1 at index 0 and 1
# 2. Get the next number by adding current number plus one and store it in respective index


def print_fibonacci(length):
    numbers_list = list()
    counter = 0

    for i in range(0, length):
        if i < 2:
            numbers_list.insert(i, i)
        else:
            numbers_list.insert(i + 1, numbers_list[-1] + counter)
            counter = numbers_list[-2]
    return numbers_list


# play = input("Play Fibonnaci game?? Y for Yes and N for No >>")
#
#
# while play == "Y" or play == "y":
#     num = int(input("Enter a number between 0 and n >> "))
#     print(print_fibonacci(num))
#     play = input("Continue Playing?? >>")
