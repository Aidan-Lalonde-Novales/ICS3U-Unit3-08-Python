#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This program tells a user if the year they
# they enter is a leap year using nested if statements


def main():
    # this function determines if a given year is a leap year

    # input
    year_input_string = input("Please enter a year: ")

    # process
    try:
        year_input = int(year_input_string)
        if year_input % 4 == 0:
            if year_input % 100 == 0:
                if year_input % 400 == 0:
                    # output
                    print("{} is a leap year.".format(year_input))
                else:
                    print("{} is not a leap year.".format(year_input))
            else:
                print("{} is a leap year.".format(year_input))
        else:
            print("{} is not a leap year.".format(year_input))
    except Exception:
        print("That is an invalid year. Please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
