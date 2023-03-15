# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver


def letter(row, col):
    if (row < 5) or (8 <= row <= 9):
        return "N"
    if (row >= 16) or (10 <= row <= 12):
        return "Z"
    if 5 <= row <= 7:
        if 5 <= col <= 10:
            return "M"
        return "N"
    if 13 <= row <= 15:
        if 5 <= col <= 10:
            return "M"
    return "Z"



if __name__ == '__main__':
    driver.comparePatterns(letter)
