#! /usr/bin/env python
import sys
import logging
from functools import wraps



def eminem(function):
	@wraps(function)
	def wrapper(*args, **kwargs):		
		with open("log.txt", "a") as myfile:
			myfile.write('start doing a thing\n')
			function(*args, **kwargs)
			myfile.write('finished doing that thing that I was doing\n')
	return wrapper

def whatever(numbers):
	return numbers+numbers

@eminem
def something(x):
	return("I'm a thing, I do some stuff", 'like this', 'and this', whatever(x), 'woo numbers')


if __name__ == '__main__':
	print(something(4)