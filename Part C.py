#! /usr/bin/env python

import turtle

def drawLeftSquare():
	t = turtle

	t.penup()
	t.home()
	t.setpos(-300,200)

	t.pendown()
	t.fd(150)
	t.rt(90)
	t.fd(150)
	t.rt(90)
	t.fd(150)
	t.rt(90)
	t.fd(150)
	t.penup()


def drawRightSquare():
	t = turtle

	t.penup()
	t.home()
	t.setpos(150,200)

	t.pendown()
	t.fd(150)
	t.rt(90)
	t.fd(150)
	t.rt(90)
	t.fd(150)
	t.rt(90)
	t.fd(150)
	t.penup()




if __name__ == '__main__':

	t = turtle

	drawLeftSquare()
	drawRightSquare()
	t.exitonclick()
