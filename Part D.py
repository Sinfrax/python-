#! /usr/bin/env python

import os
import sys

def calculateNumberOfFilesAndFoldersInPWD():
	'''Prints the number of files and folders in directory'''
	array = (os.listdir('./'))
	return len(array)


if __name__ == '__main__':

	os.chroot(sys.argv)
	calculateNumberOfFilesAndFoldersInPWD()