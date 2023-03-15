# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver


def letter(row, col):
    if row == 0 or row == 1 or 7 <= row <= 9:
        return "K"
    if row == 10:
        return "B"
    if 2 <= row <= 3:
        if col <= 3 or col >= 10:
            return "K"
        if 4 <= col <= 9:
            return "Y"
    if 4 <= row <= 5:
        if col <= 3 or col >= 13:
            return "K"
        if 4 <= col <= 6:
            return "Y"
        if 7 <= col <= 9:
            return "X"
        if 10 <= col <= 12:
            return "B"
    if row == 6:
        if col <= 6 or col >= 13:
            return "K"
        if 7 <= col <= 12:
            return "B"


if __name__ == '__main__':
    driver.comparePatterns(letter)
