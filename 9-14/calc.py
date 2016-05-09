#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

def isum(a, b):
	return a + b

def minus(a,b):
	return a - b

def multiplication(a, b):
	return a * b

def division(a, b):
	return float(a) / b

def mod(a, b):
	return a % b

operate = {'+':isum, '-':minus, '*':multiplication,\
 '/':division, '%':mod, '^':pow}


def calc(a, b, c):
	try:
		a1 = float(a)
		c1 = float(c)
	except ValueError, e:
		raise ValueError, e
	b1 = b.strip()
	if not b1 in operate.keys():
		raise ValueError, 'must [+ - * / % ^]'
	rs = operate[b1](a1, c1)
	with open('calc_log.txt', 'a') as txt_obj:
		for i in (a.strip(), b1, c.strip()):
			txt_obj.write(i + ' ')
		else:
			txt_obj.write(os.linesep + str(rs) + 
				os.linesep)
	return rs


if __name__ == '__main__':
	user_input = sys.argv[1:4]
	if len(user_input) == 1:
		if user_input[0] == 'print':
			with open('calc_log.txt', 'r+') as txt_obj:
				for i in txt_obj:
					print i,
			obj = open('calc_log.txt', 'w')
			obj.close()

		else:
			raise TypeError, "you can enter [print] to show"
	elif len(user_input) == 3:
		print calc(user_input[0], user_input[1], user_input[2])
	else:
		raise TypeError, "unsupported operate please check!"