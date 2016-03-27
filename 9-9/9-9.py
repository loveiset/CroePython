#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

def docStr(obj_path):
	obj_list = os.listdir(obj_path)
	f = open('ass.txt', 'w')
	f.write('Have __doc__:' + os.linesep)
	no_doc = []
	for filename in obj_list:
		if filename.endswith('.py'):
			print filename, '--ing'
			try:
				temp = __import__(os.path.splitext(filename)[0])
				if temp.__doc__ is None:
					no_doc.append(filename)
				else:
					f.write(filename+':'+os.linesep+temp.__doc__)
					f.write(os.linesep)
					f.write('-' * 20)
					f.write(os.linesep)
					f.write(os.linesep)
			except ImportError:
				print 'IGNORE %s' % filename

	f.write('No __doc__:' + os.linesep)
	for i in no_doc[:-1]:
		f.write(i + ',')
	f.write(no_doc[-1])

	f.close()

docStr('/usr/lib/python2.7')

