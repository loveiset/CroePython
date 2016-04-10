#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
(a)编写一个URL书签管理程序。使用基于文本的菜单，用户可以添加、修改或者删除书签数据项，书签数据项中包含站点名称、
URL和一行简单说明（可选）。另外提供检索功能，可以根据检索关键字在站点名称和URL两部分查找可能的匹配。程序退出时
把数据保存到一个磁盘文件中去，再次执行时加载保存的数据。
(b)改进(a)的方案，把书签输出到一个合法且语法正确的HTML文件中，这样用户就可以使用浏览器查看自己的书签清单。另外
提供创建“文件夹”功能，对相关的书签进行分组管理。

附加题：请阅读Python的re模块了解有关的正则表达式的资料，使用正则表达式对用户输入的URL进行验证。
'''

import pickle  #持久化


def add_url():  #添加
	newURL = []
	URLname = raw_input('请输入储存的URL名称： ').decode('utf-8')
	newURL.append(URLname)
	URLdomain = raw_input('请输入URL地址： ').decode('utf-8')
	newURL.append(URLdomain)
	URLremark = raw_input('备注（可选）： ').decode('utf-8')
	newURL.append(URLremark)
	URLDate.append(newURL)

def view():
	print u'编号 | 名称 | 地址 | 备注'
	for index in range(len(URLDate)):
		print '%d | %s | %s | %s ' % \
		(index, URLDate[index][0], URLDate[index][1], URLDate[index][2])

def alter_url():  #修改
	view()
	idx = input('选择一个编号修改：')
	print u'修改对象'
	print '%d | %s | %s | %s ' % \
		(idx, URLDate[idx][0], URLDate[idx][1], URLDate[idx][2])
	URLname = raw_input('请输入储存的URL名称：    跳过请按q\n').decode('utf-8')
	if URLname == 'q':
		pass
	else:
		URLDate[idx][0] = URLname
	URLdomain = raw_input('请输入URL地址：      跳过请按q\n').decode('utf-8')
	if URLdomain == 'q':
		pass
	else:
		URLDate[idx][1] = URLdomain
	URLremark = raw_input('备注（可选）：       跳过请按q\n').decode('utf-8')
	if URLremark == 'q':
		pass
	else:
		URLDate[idx][2] = URLremark

def delete_url():  #删除URL
	print u'编号 | 名称 | 地址 | 备注'
	for index in range(len(URLDate)):
		print '%d | %s | %s | %s ' % \
		(index, URLDate[index][0], URLDate[index][1], URLDate[index][2])
	idx = input('选择一个编号删除： ')
	print u'删除成功：'
	print URLDate.pop(idx)

def findkey():  #根据名称和地址检索
	cStr = raw_input('请输入需要查找的关键字： ').strip().decode('utf-8')
	result = []
	for index in range(len(URLDate)):
		if URLDate[index][0].find(cStr) != -1:
			result.append(index)
			print u'|名称： %s |地址： %s |备注： %s ' % \
		    (URLDate[index][0], URLDate[index][1], URLDate[index][2])
		if URLDate[index][1].find(cStr) != -1:
			result.append(index)
			print u'|名称： %s |地址： %s |备注： %s ' % \
		    (URLDate[index][0], URLDate[index][1], URLDate[index][2])
	if result == []:
		print u'没有查到相关信息'

def menu():
    try:
    	fObj = open('url.txt', 'r')
    	global URLDate
    	URLDate = pickle.load(fObj)
    	
    except IOError:
    	
    	URLDate = []

    global text, choseDict

    choseDict = {'A': add_url, 'M': alter_url, 
    'D': delete_url, 'V': view, 'F': findkey}


    text = '''
-----------欢迎使用Python书签管理系统-----------

请选择相应的按钮：
       添加：              A
       修改：              M
       删除：              D
       查看：              V
       搜索：              F
       退出：              Q

>'''
    while True:
    	ch = raw_input(text).strip().upper()
    	if ch not in 'AMDVQF':
    		print u'输入无效，请重新输入'
    		continue
    	if ch == 'Q':
    		break
    	choseDict[ch]()

    
    pickle.dump(URLDate, open('url.txt', 'w'))

if __name__ == '__main__':
	menu()