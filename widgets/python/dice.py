#!/usr/bin/python3
#835B0032-Legacy
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "\n-----------\nRolling the dices...\n"
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again? ")

