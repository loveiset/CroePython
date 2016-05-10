#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def handle_line(long_line):         #处理行数大于80的行，返回含有多行的列表
	small_line = []
	count = len(long_line)/80
	for i in range(count):
		indenx = long_line[:80].rfind(' ')        #找出以第80字为左边的空格
		small_line.append(long_line[:indenx] + os.linesep)
		long_line = long_line[indenx+1:]
	small_line.append(long_line + os.linesep)
	return small_line
			

if __name__ == '__main__':
	target_txt = raw_input('截短的文件对象：')
	target_txt_obj = open(target_txt, 'r')
	new_txt = []     # 存放新的文件内容

	for line in target_txt_obj:
		if len(line) > 80:
			new_line = handle_line(line)
			new_txt.extend(new_line)
		else:
			new_txt.append(line + os.linesep)
	target_txt_obj.close()

	with open(os.path.splitext(target_txt)[0] + \
		'(1)' + os.path.splitext(target_txt)[1], 'w') as f:   #输出副本
		f.writelines(new_txt)
	print '输出新文件成功！'
