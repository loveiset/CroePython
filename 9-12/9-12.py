#!/usr/bin/env python
# -*- coding: utf-8 -*- 


"""
用户名和密码.回顾练习7-5,修改代码使之可以支持"上次登录时间".
请参阅time模块中的文档了解如何记录用户上次登录的时间.
另外提供一个"系统管理员",它可以导出所有用户的用户名,密码(如果
想要的话，你可以把密码加密),以及"上次登录时间。
"""


import time, hashlib, shelve, getpass, string

db = shelve.open('user.data')  #shelve对象 用于存储数据

def newuser():     #新用户注册
	prompt = 'Login desired: '
	userdict = string.digits + string.lowercase
	while True:
		chosen = False
		name = raw_input(prompt).lower()
		for i in name:                        #只允许字母和数字
			if i not in userdict:
				chosen = True
				break
		if db.has_key(name):
			prompt = 'Name taken, try another:'
		elif chosen:
			prompt ='user name only use letters of an alphabet \
and digits!\n>'
		else:
			break
	pwd = hashlib.md5(getpass.getpass('Password: ')).hexdigest()
	timeStamp = time.time()  #记录时间戳
	db[name] = [pwd, timeStamp]

def olduser():   #用户登入
	name = raw_input('Login: ').lower()
	if db.has_key(name):
		pwd = hashlib.md5(getpass.getpass('Password: ')).hexdigest()
		new = time.time()
		old = db.get(name)[1]
		passwd = db.get(name)[0]
		if passwd == pwd:
			print 'Welcome back', name
			if int(new) - int(old) <= 4*3600:  #判断是否是四小时之内登入过
				print time.strftime(
					"You already logged in at: %X", time.localtime(old))
			db[name][1] = new
		else:
			print 'login incorrect'
	else:
		prompt = "User not exist, register enter 'Y'.\n>"  #如果用户不存在，询问是否创建
		choice = raw_input(prompt).strip()[0].upper()
		if choice == 'Y':
			newuser()

def admin():        #管理员操作
	root = raw_input('user: ').lower()
	chosen = True
	pwd = getpass.getpass('password: ')
	if root == 'root' and pwd == '123456':
		print 'Root!'
		while chosen:
			prompt = """
(V)iew all users
(D)eleta a user
(E)xport data
(Q)uit
>"""
			choice = raw_input(prompt).upper()
			if choice not in 'VDQE':
				print "invalid option try again"
			else:
				if choice == 'V':  #查看用户
					print '%-10s%-30s%s' % ('name', 'time', 'pwd')
					for user in db:
						print '%-10s%-30f%s' % \
						(user, db[user][1], db[user][0])
				if choice == 'D':  #删除用户
					name = raw_input("deleted user name: ").lower()
					print 'deleted %s' % name
					del db[name]
				if choice == 'Q':
					chosen = False
				if choice == 'E':   #导出信息选项
					f_obj = open('user.txt', 'w')
					for user in db:
						f_obj.write('%s: %s: %f\n' % \
						(user, db[user][0], db[user][1]))
					f_obj.close()
					print 'export succed!'
	else:
		print 'invalid admin ID!'


def showmenu():
	prompt = """
(N)ew User Login
(E)xisting User Login
(A)dministrator Login
(Q)uit

Enter choice:"""

	done = False
	while not done:

		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError, KeyboardInterrupt):
				choice = 'q'
			print '\nYou picked: [%s]' % choice
			if choice not in 'neqa':
				print 'invalid option, try again'
			else:
				chosen = True

		if choice == 'q': done = True
		if choice == 'n': newuser()
		if choice == 'e': olduser()
		if choice == 'a': admin()

if __name__ == '__main__':
	showmenu()
	db.close()