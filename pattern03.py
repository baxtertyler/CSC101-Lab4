# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver


def letter(row, col):
    if col <= 9:
        return "D"
    return "P"


if __name__ == '__main__':
    driver.comparePatterns(letter)
