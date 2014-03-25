#! /usr/bin/env python

import unittest
import subprocess

class testPartA(unittest.TestCase):
	def test_part_a(self):
		'''test part A.py'''
		self.assertEqual(
			'3\n',
			subprocess.check_output(('python', 'part A.py', '1', '2', '3')))


if __name__ == '__main__':
	unittest.main()