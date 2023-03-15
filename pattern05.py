# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver

"""
def letter(row, col):
    if row == 0:
        return "U"
    if row == 1:
        if col <= 0:
            return "B"
        else:
            return "U"
    if row == 2:
        if col <= 1:
            return "B"
        else:
            return "U"
    if row == 3:
        if col <= 2:
            return "B"
        else:
            return "U"
    if row == 4:
        if col <= 3:
            return "B"
        else:
            return "U"
    if row == 5:
        if col <= 4:
            return "B"
        else:
            return "U"
    if row == 6:
        if col <= 5:
            return "B"
        else:
            return "U"
    if row == 7:
        if col <= 6:
            return "B"
        else:
            return "U"
    if row == 8:
        if col <= 7:
            return "B"
        else:
            return "U"
    if 9 <= row <= 11:
        if col <= 10:
            return "B"
        else:
            return "U"
    if row == 12:
        if col <= 11:
            return "B"
        else:
            return "U"
    if row == 13:
        if col <= 12:
            return "B"
        else:
            return "U"
    if row == 14:
        if col <= 13:
            return "B"
        else:
            return "U"
    if row == 15:
        if col <= 14:
            return "B"
        else:
            return "U"
    if row == 16:
        if col <= 15:
            return "B"
        else:
            return "U"
    if row == 17:
        if col <= 16:
            return "B"
        else:
            return "U"
    if row == 18:
        if col <= 17:
            return "B"
        else:
            return "U"
    if row == 19:
        if col <= 18:
            return "B"
        else:
            return "U"
"""


def letter(row, col):
    if row <= 8:
        if row <= col:
            return "U"
        else:
            return "B"
    if row >= 12:
        if row <= col:
            return "U"
        else:
            return "B"
    if 9 <= row <= 11:
        if col <= 10:
            return "B"
        else:
            return "U"


if __name__ == '__main__':
    driver.comparePatterns(letter)
