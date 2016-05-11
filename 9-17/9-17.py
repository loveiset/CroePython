#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def create_file():
	ms = raw_input('Enter your file name: ')
	print '''You can input you text some lines.
And "Q" to quit.\n'''
	text = []        #写入的内容放入列表中
	n = 0            #初始化行数
	while True:
		n += 1
		line = raw_input("%s " % n)
		if line == 'Q':
			break
		else:
			text.append(line + os.linesep)
	with open(ms, 'w') as f:
		f.writelines(text)

def print_file():
	ms = raw_input('Enter you print file name: ')
	try:
		with open(ms, 'r') as f:
			n = 0
			for i in f:
				n += 1
				print n, i,
	except IOError, e:
		print 'check your name: ', e

def edit_file():
	ms = raw_input('Enter your edit file name: ')
	with open(ms, 'r+') as f:
		rs = f.readlines()
		line_num = input('edite line number: ')
		print rs[line_num - 1],
		rs[line_num-1] = raw_input('Change: ') + os.linesep
		f.seek(0, 0)
		f.writelines(rs)


if __name__ ==  '__main__':
	menu = '''
Please Chose a alphabet:
(C)rete file
(P)rint file
(E)dit file
(Q)uit 
>'''
	while True:
		chose = raw_input(menu).strip()[0].upper()
		if chose == 'C':
			create_file()
		elif chose == 'P':
			print_file()
		elif chose == 'E':
			edit_file()
		elif chose == 'Q':
			break
		else:
			print '\nYour enter invaild please enter again!'
