#! /usr/bin/env python

import unittest
import subprocess

class testPartA(unittest.TestCase):
	def test_part_c(self):
		self.assertEqual(
			'3\n',
			subprocess.check_output(('python', 'Part C.py')))

if __name__ == '__main__':
	unittest.main()