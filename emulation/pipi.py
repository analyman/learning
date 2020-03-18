#!/usr/bin/env python3

""" approximation of pi base on random """

import random
import math
import sys


def inpi():
    x: int = random.random() * 2 - 1
    y: int = random.random() * 2 - 1
    if (math.pow(x, 2) + math.pow(y, 2)) <= 1:
        return True
    else:
        return False


def usage():
    print("pipi <n>")


def pi(num: int) -> float:
    n: int = num
    m: int = 0
    while n > 0:
        if inpi():
            m += 1
        n -= 1
    return 4.0 * m / num


def main():
    try:
        totaltest: int = int(sys.argv[1])
        if totaltest <= 333333:
            totaltest = 333333
    except(Exception):
        usage()
        exit(1)
    pipi: float = pi(totaltest)
    print("pi = {0}".format(pipi))


if __name__ == '__main__':
    main()
