# Lab 4
#
# Name: Tyler Baxter
# Instructor: Sussan Einakian
# Section: 03

import driver


def letter(row, col):
    if row % 2 == 0 and col < 3:
        return "L"
    if row % 2 == 0 and col >= 3:
        return "G"
    if row % 2 == 1 and col < 17:
        return "G"
    if row % 2 == 1 and col >= 17:
        return "O"


if __name__ == '__main__':
    driver.comparePatterns(letter)
