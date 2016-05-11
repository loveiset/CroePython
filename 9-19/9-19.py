#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string, random

def new(file_path, ct, n, sum_char):
	a_string = list()

	for i in range(sum_char-len(ct)*n):
		a_string.append(random.choice(string.printable))

	temp = ''.join(a_string).count(ct)

	for i in range(n-temp):
		a_string.insert(random.randint(0, sum_char-len(ct)*n-1), ct)

	with open(file_path, 'w') as f:
		f.writelines(a_string)

if __name__ == '__main__':
	file_obj = raw_input('File： ')
	count_obj = raw_input('Char: ')
	num = input('appear times: ')
	sum_char = input('Size: ')

	new(file_obj, count_obj, num, sum_char)