#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''家庭理财，创建一个家庭理财程序。你的程序需要处理储蓄、支票、金融市场，定期存款等多种账户。
为每种账户提供一个菜单操作界面，要有存款、取款、借、贷等操作。另外还要提供一个取消操作选项。
用户退出这个程序时相应的数据应保存到文件中。（出去备份的目的，程序运行的过程中也要备份）'''

import os
import shelve   #数据储存
from shutil import copy  #备份

def user():
	while 1:
		name = raw_input("请输入你的姓名：(返回上级菜单请按'E') > ")
		if name == 'E':
			break
		if (name + '.dat') not in os.listdir(os.getcwd()):
			f_obj = shelve.open(name + '.dat')
			f_obj['deposit'] = 0
			f_obj['withdraw'] = 0
			f_obj['loan'] = 0
			f_obj['credit'] = 0
			f_obj['moneySum'] = 0
			f_obj.close()
			break
		else:
			print u'用户已存在，请检查重新输入。'

def operate(name):
	"主程序写入数据"
	copy(name + '.dat', name + '.backup')
	while True:
		choice = raw_input('''
存款\t\t请按'D'
取款\t\t请按'W'
借款\t\t请按'L'
贷款\t\t请按'C'
返回上级\t请按'E'
>''').strip()[0].upper()
		if choice in 'DWLCE':
			break
		else:
			print u'输入错误，请重新输入'
	if choice == 'E':
		return None
	f_obj = shelve.open(name + '.dat', writeback=True)
	money = float(input('请输入金额： '))
	if choice == 'D':
		f_obj['deposit'] += money
	elif choice == 'W':
		f_obj['withdraw'] += money
	elif choice == 'L':
		f_obj['loan'] += money
	else:
		f_obj['credit'] += money
	f_obj['moneySum'] = f_obj['deposit'] - f_obj['withdraw'] -\
	f_obj['loan'] + f_obj['credit']
	f_obj.close()

def view(name):
	if name + '.dat' in os.listdir(os.getcwd()):
		f_obj = shelve.open(name + '.dat')
		print u'存款%10.2f' % f_obj['deposit']
		print u'取款%10.2f' % f_obj['withdraw']
		print u'借款%10.2f' % f_obj['loan']
		print u'贷款%10.2f' % f_obj['credit']
		print u'总额%10.2f' % f_obj['moneySum']
		f_obj.close()
	else:
		print '用户不存在！'

def menu():
	tag = False
	while not tag:		
		aString = '''
请选择要操作的内容：
创建新用户\t\t\t请按'N'
查看信息\t\t\t请按'L'
家庭记账\t\t\t请按'W'
退出\t\t\t\t请按'Q'
>'''
		choice = raw_input(aString).strip().upper()
		if choice not in 'NLWQ':
		    print '输入不合法，请重新选择！'
		    continue
		if choice == 'Q':
			tag = True
			continue
		if choice == 'N':
			user()	
		if choice == 'L':
			name = raw_input('请输入你的姓名：')
			view(name)
		if choice == 'W':
			name = raw_input('请输入你的姓名：')
			if name + '.dat' in os.listdir(os.getcwd()):
				operate(name)
			else:
				print '用户不存在！'

if __name__ == '__main__':
	menu()