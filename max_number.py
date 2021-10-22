#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# this is the max number program in python
# finds the largest number out of 10 randomly generated numbers and prints it
# this program uses arrays as parameter

import random


def largest_number(random_number_list):
    # this function finds the biggest number in the list
    # finds the max number

    max_number = random_number_list[1]

    for loop_counter in random_number_list:
        if loop_counter > max_number:
            max_number = loop_counter

    return max_number


def main():
    # this function uses a list
    # this function gets generates random number

    random_number_list = []
    # loop_counter = 0

    print("Here is a list of 10 randomly generated numbers:")
    print(" ")
    for loop_counter in range(1, 11):
        single_number = random.randint(1, 100)
        random_number_list.append(single_number)
        # loop_counter = loop_counter + 1
        print("Random number {0} is : {1}".format(loop_counter, single_number))

    # call function
    bigger_number = largest_number(random_number_list)

    # output
    print("\nThe largest number is {0}.".format(bigger_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
