#! /usr/bin/env python

import os

def calculateNumberOfFilesAndFoldersInPWD():
	'''Prints the number of files and folders in current working directory'''
	
	return len(os.listdir(os.getcwd()))


if __name__ == '__main__':

	print calculateNumberOfFilesAndFoldersInPWD()
