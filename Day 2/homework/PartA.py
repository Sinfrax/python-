#! /usr/bin/env python
import sys

def factorial(x):
    base = 1
    if x>1:
        base = x*factorial(x-1)
        print base
    return base

if __name__ == '__main__':

    print factorial(10)