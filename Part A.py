#! /usr/bin/env python
import sys

def calculateNumberOfPerameters(x):
	'''Prints the number of params in function'''
	return (len(x) - 1)


if __name__ == '__main__':
	print calculateNumberOfPerameters(sys.argv)