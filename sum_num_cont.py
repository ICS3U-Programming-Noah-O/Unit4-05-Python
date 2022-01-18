#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 13, 2022
# This program allows a user to select a number of numbers
# to add together and then select what numbers they want to add together

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():

    # Print intro message
    print(Fore.WHITE + "This program adds a number of numbers together.")
    print(Fore.BLUE + " ")
    sum = 0

    # Loop that asks the user for the number of numbers they want to add
    while True:

        user_loop_num = (input("How many numbers would you like to add? "))
        try:
            # Make sure user input is an integer
            user_loop_num_int = int(user_loop_num)

            # Makes sure that user number is positive
            if user_loop_num_int > 0:
                # Loop that asks the user for what integers
                # they want to add together and makes
                # sure that all inputs are valid
                time.sleep(1)
                print(Fore.CYAN + " ")
                counter = 0
                total_sum = "Sum = 0"
                while counter < user_loop_num_int:
                    counter = counter + 1
                    user_num_add = input("Enter a number: ")

                    # Make sure that the input is an integer
                    try:
                        user_num_add_int = int(user_num_add)

                        # Make sure that the input is above 0
                        if user_num_add_int <= 0:
                            counter = counter - 1
                            print("Input must be a " +
                                  "positive integer to be added.")
                            continue
                        else:

                            print("Added {} to ".format(user_num_add_int) +
                                  "total.")
                            sum_str = str(user_num_add_int)
                            total_sum = total_sum + " + " + sum_str
                    # Cathces any invalid inputs
                    except Exception:
                        counter = counter - 1
                        print("Input must be an integer.")
                        continue

                    print(" ")
                    sum = sum + user_num_add_int

                # Print final sum
                print(total_sum)
                print("Sum = {}".format(sum))
                break

            else:
                print("{} is not a positive number.".format(user_loop_num_int))

        except Exception:
            # Prevent crash by displaying error message if user
            # input is not an integer
            print(" ")
            print("'{}' is not a number".format(user_loop_num))


if __name__ == "__main__":
    main()
