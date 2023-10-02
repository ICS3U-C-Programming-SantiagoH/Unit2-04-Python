#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Sep 30, 2023
# This program asks the user for the size of
# a pizza in inches. It then calculates and displays
# the subtotal, tax and total of tha pizza.

import constants


def main():
    # get the size in inches from the user
    print("This program will calculate the price of your pizza")
    print("with your size input in inches.")
    diameter_in_inches = float(input("Enter the size you want (in): "))

    # declare variable
    MATERIALS = 1.50 * diameter_in_inches

    # calculates the subtotal
    subtotal = constants.RENT + constants.LABOR + MATERIALS

    # calculates the tax
    tax = subtotal * constants.HST

    # calculates the total
    total = subtotal + tax

    # display the subtotal
    print("")
    print("The subtotal of your pizza is = ${:.2f}".format(subtotal))

    # display the tax
    print("")
    print("The tax of your pizza is = ${:.2f}".format(tax))

    # display the total
    print("")
    print("The total of your pizza is = ${:.2f}".format(total))


if __name__ == "__main__":
    main()
