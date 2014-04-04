#! /usr/bin/env python
import sys

def checkIfNumberIsEven(num):
	if num%2==0 and num!=2:
		return True


def checkIfNumberIsPrime(num):
    if checkIfNumberIsEven(num) == True:
    	return
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True


if __name__ == '__main__':
    for i in range(int(sys.argv[1]),int(sys.argv[2])):
    	if checkIfNumberIsPrime(i) == True:
        	print i
