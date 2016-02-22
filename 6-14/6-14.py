#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Rochambeau():
	import random
	you_d = raw_input('''
你的判断:
1\t\t石头
2\t\t剪刀
3\t\t布
>''')
	doc_dict = {1:'石头', 2:'剪刀', 3:'布'}
	machine = random.choice([1,2,3])
	win_dict = {1:2, 2:3, 3:1}
	if int(you_d.strip()) == machine:
		print '平局，都是%s' % doc_dict[machine]
	elif win_dict[int(you_d.strip())] == machine:
		print '恭喜你，你赢了！人家出了%s' % doc_dict[machine]
	else:
		print '对不起，你输了！人家出了%s' % doc_dict[machine]

if __name__ == '__main__':
	while 1:
		try:
			Rochambeau()
		except (ValueError, KeyError, EOFError, KeyboardInterrupt):
			break