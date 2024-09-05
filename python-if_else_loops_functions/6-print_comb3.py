#!/usr/bin/python3
for isagi in range(10):
    for lacazette in range( isagi + 1, 10):
        if isagi == 8 and lacazette == 9:
            print(f"{isagi}{lacazette}".format(isagi, lacazette))
        else:
            print(f"{isagi}{lacazette}, ".format(isagi, lacazette), end="")
