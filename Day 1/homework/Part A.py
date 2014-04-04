#! /usr/bin/env python
import sys

def calculateInterestRate3(whole, year):
	'''Calculate 3 percent interest rate for value'''
	return whole*(1 + 0.03)**year

def calculateInterestRate5(whole):
	'''Calculate 7 percent interest rate for value'''
	return whole*(1 + 0.05)**10


def calculateInterestRate7(whole):
	'''Calculate 10 percent interest rate for value'''
	return whole*(1 + 0.07)**10


if __name__ == '__main__':

	for i in range(0,10):
		print 'year '+i+' at 3% ='+calculateInterestRate3(float(sys.argv[1]), i)
	

	for (var i=0;i<10;i++){
		print calculateInterestRate3(float(sys.argv[1]), i)
	}


	print 'year '+i+' at 5% ='+calculateInterestRate5(float(sys.argv[1]))
	print 'year '+i+' at 7% ='+calculateInterestRate7(float(sys.argv[1]))
