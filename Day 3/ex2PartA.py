#! /usr/bin/env python


class ascii(object):
	def drawTriangle(self):
		print'\n'
		print'       *       '
		print'      * *      '
		print'     *   *     '
		print'    *     *    '
		print'   *       *   '
		print'  *         *  '
		print' *           * '
		print'* * * * * * * *'
		print'\n'


	def drawSquare(self):
		print'\n'
		print'* * * * * * * *'
		print'*             *'
		print'*             *'
		print'*             *'
		print'*             *'
		print'*             *'
		print'*             *'
		print'* * * * * * * *'
		print'\n'


	def drawerRectangle(self):
		print'\n'
		print'* * * * * * * * * * * * * * * * * * * *'
		print'*                                     *'
		print'*                                     *'
		print'*                                     *'
		print'*                                     *'
		print'*                                     *'
		print'*                                     *'
		print'* * * * * * * * * * * * * * * * * * * *'
		print'\n'


if __name__ == '__main__':
	object = ascii()
	object.drawTriangle()
	object.drawSquare()
	object.drawerRectangle()