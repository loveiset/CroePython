#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
ls=os.linesep

def write():
	while True:
		fname=raw_input('Enter file name:')
		if os.path.exists(fname):
			print('Error %s already exists ' % fname)
		else:
			break
	all=[]
	print("\nEnter lines ('.' by itself to quit).\n")
	while True:
		entry=raw_input('>')
		if entry=='.':
			break
		else:
			all.append(entry)
	fobj=open(fname,'w')
	fobj.writelines(['%s%s' % (x,ls) for x in all])
	fobj.close()
	print('Done')

def read():

	newtext = []

	while True:
		fname=raw_input('Enter filename:')
		if not os.path.exists(fname):
			print('sorry,%s is not exists' % fname)
		else:
			break
	try:
		fobj=open(fname,'r')
	except IOError as e:
		print("*** file open error" ,e)
	else:
		for eachline in fobj:
			print eachline
			che = raw_input("enter 'e' edit, else jump>>")
			if che == 'e':
				neachline = raw_input('NEW:')
				newtext.append(neachline)
			else:
				newtext.append(eachline.strip())
		fobj.close()
	nfobj = open(fname, 'w')
	nfobj.writelines(["%s%s" % (i, ls) for i in newtext])
	nfobj.close()

uu = 1
while uu not in ('q', 'r', 'w'):
	uu = raw_input('''
		-------------
		r        read
		w       write
		q        quit
		-------------
		''')
	if uu == 'q':
		break
	elif uu == 'r':
		read()
	elif uu == 'w':
		write()
	else:
		uu = 1