# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver

"""
def letter(row, col):
    if row == 0 or row == 8:
        return "C"
    if row == 1 or row == 7:
        if col == 0 or col == 8:
            return "C"
        if col == 1 or col == 7:
            return "E"
        return "O"
    if row == 2 or row == 6:
        if col == 0 or col == 8:
            return "C"
        if col == 2 or col == 6:
            return "E"
        if col == 1 or col == 7 or 3 <= col <= 5:
            return "O"
    if row == 3 or row == 5:
        if col == 0 or col == 8:
            return "C"
        if 1 <= col <= 2 or 6 <= col <= 7 or col == 4:
            return "O"
        if col == 3 or col == 5:
            return "E"
    if row == 4:
        if col == 0 or col == 8:
            return "C"
        if 1 <= col <= 3 or 5 <= col <= 7:
            return "O"
        if col == 4:
            return "E"
"""


def letter(row, col):
    if (row == 0) or (row == 8) or (col == 0) or (col == 8):
        return "C"
    if (row == col) or (row == 8 - col):
        return "E"
    else:
        return "O"


if __name__ == '__main__':
    driver.comparePatterns(letter)
