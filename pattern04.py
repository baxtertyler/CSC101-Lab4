# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver


def letter(row, col):
    if (row == 0) or (row == 8):
        return "W"
    if (1 <= row <= 2) or (6 <= row <= 7):
        return "S"
    else:
        if (0 <= col <= 2) or (7 <= col <= 9):
            return "S"
        else:
            return "W"


if __name__ == '__main__':
    driver.comparePatterns(letter)
