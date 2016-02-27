#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def product_matrix(a_matrix, b_matrix):
	a_len_row = len(a_matrix)
	a_len_column = len(a_matrix[0])
	b_len_row = len(b_matrix)
	b_len_column = len(b_matrix[0])
	if a_len_column == b_len_row:
		result_matrix = [[0]*b_len_column for i in range(a_len_row)]
		for x in range(a_len_row):
			for y in range(b_len_column):
				for z in range(a_len_column):
					result_matrix[x][y] += a_matrix[x][z] * b_matrix[z][y]
		return result_matrix
	else:
		return u'ERROR! 矩阵a的列和矩阵b的行不想等!不能相乘。%s' % os.linesep

def add_matrix(a_matrix, b_matrix):
	a_len_row = len(a_matrix)
	a_len_column = len(a_matrix[0])
	b_len_row = len(b_matrix)
	b_len_column = len(b_matrix[0])
	if a_len_row == b_len_row and a_len_column == b_len_column:
		result_matrix = [[0]*a_len_column for i in range(a_len_row)]
		for x in range(a_len_row):
			for y in range(a_len_column):
				result_matrix[x][y] = a_matrix[x][y] + b_matrix[x][y]
		return result_matrix
	else:
		return u'Error! 矩阵a的行和列不与矩阵b的行和列相等！不能相加。%s' % os.linesep

if __name__ == '__main__':
	a_matrix_rows = input('请输入第一个矩阵的行数：')
	a_matrix_columns = input('请输入第一个矩阵的列数：')
	a_matrix = [[0]*a_matrix_columns for i in range(a_matrix_rows)]
	for x in range(a_matrix_rows):
		for y in range(a_matrix_columns):
			values = input('请输入第一个矩阵%d行%d列的值：' % (x+1, y+1))
			a_matrix[x][y] = values
		print '第%d行输入完毕。' % (x+1)
	else:
		print '第一个矩阵输入完成'

	b_matrix_rows = input('请输入第二个矩阵的行数：')
	b_matrix_columns = input('请输入第二个矩阵的列数：')
	b_matrix = [[0]*b_matrix_columns for i in range(b_matrix_rows)]
	for x in range(b_matrix_rows):
		for y in range(b_matrix_columns):
			values = input('请输入第二个矩阵%d行%d列的值：' % (x+1, y+1))
			b_matrix[x][y] = values
		print '第%d行输入完毕。' % (x+1)
	else:
		print '第二个矩阵输入完毕'

	chose_dict = dict([(0,add_matrix), (1,product_matrix)])
	chose_value = input('''
请选择数字如何操作：
0\t\t两个矩阵相加
1\t\t两个矩阵相乘
>''')
	print chose_dict[chose_value](a_matrix, b_matrix)