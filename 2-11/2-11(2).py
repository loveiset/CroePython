#!/usr/bin/env python
# -*- coding: utf-8 -*-


def visual():
	while 1:
		mSelect = raw_input('''
			-----------
			1       求和
			2      求平均
			q       退出
			-----------
			>''')

		if mSelect == '1':
			mSum = 0
			try:
				for i in range(5):
					mValues = int(raw_input('请输入第%d个数字:' % (i + 1)))
					mSum += mValues
			except ValueError, e:
				print '输入非法字符：', e
			print '所求和为：%d' % mSum

		elif mSelect == '2':
			mSum = 0
			try:
				for i in range(5):
					mValues = int(raw_input('请输入第%d个数字:' % (i + 1)))
					mSum += mValues
			except ValueError, e:
				print '输入非法字符：', e
			print '所求平均为：%f' % (float(mSum) / 5)

		elif mSelect == 'q':
			break

		else:
			print '输入错误，请重新输入！'

if __name__ == '__main__':
	visual()