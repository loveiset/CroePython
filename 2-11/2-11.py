#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_commond():
	support_commond = ['1', '2', 'x']
	enter_commond = raw_input('''
		请输入以下命令，并按回车按钮
		-----------------------
		1             sum[list]
		2             avg[list]
		x                  quit
		-----------------------
		>''')
	if enter_commond in support_commond:
		return enter_commond
	else:
		print '输入的命令不正确'
		get_commond()

def get_list():
	i_list = raw_input('''
		请输入以下选项，并按回车继续
		-----------------------
		计算值以逗号分隔    计算对象
		q                  quit
		-----------------------
		>''').split(',')
	return i_list


ecommond = get_commond()
while ecommond in ['1', '2']:
	esum = 0
	evalues = get_list()

	if evalues == ['q']:
		break

	try:
		for i in evalues:
			esum += int(i)
	except ValueError, e:
		print '无效的字符', e
		break

	if ecommond == '1':
		print 'This is sum %d' % esum

	if ecommond == '2':
		print 'This is avg %f' % (float(esum) / len(evalues))

	ecommond = get_commond()