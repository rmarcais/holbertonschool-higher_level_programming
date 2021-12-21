#!/usr/bin/python3
for a in range(0, 10):
    for b in range(1, 10):
        if a < b:
            print("{}".format(a), end="")
            if a != 8:
                print("{}".format(b), end=", ")
            else:
                print("{}".format(b))
