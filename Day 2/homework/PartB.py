#! /usr/bin/env python
import sys
import random

def generateHexDigit(x):
	hexDigit = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	block = []
	for i in range(x):
		block+=random.sample(hexDigit,2)
	final=''.join(block)
	return final


def generateUUID():
	timeLow = generateHexDigit(4)
	timeMid = generateHexDigit(2)
	timeHighAndVersion = generateHexDigit(2)
	clockSeqAndReserved = generateHexDigit(1)
	clockSeqLow = generateHexDigit(1)
	node = generateHexDigit(6)

	UUID = timeLow+'-'+timeMid+'-'+timeHighAndVersion+'-'+clockSeqAndReserved+clockSeqLow+'-'+node
	return UUID


if __name__ == '__main__':
    print generateUUID()