#!/usr/bin/python3

# write a program that prints the ASCII alphabet,
# in lowercase, not followed by a new line.

for ch in range(97, 123):
    print("{:c}".format(ch), end="")
