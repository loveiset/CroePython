#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Payment(balance, mon_pay):
	
	index = 0
	print '\n\tAmount Remaining'
	print 'Pymt#\tPaid\t\tBalance'
	print '-----\t------\t\t--------'
	print '0\t$ 0.00\t\t$%6.2f' % float(balance)
	while balance - mon_pay > 0:
		index += 1
		balance -= mon_pay
		print '%d\t$%5.2f\t\t$%6.2f' % (index, mon_pay, balance)
	print '%d\t$%5.2f\t\t$%6.2f\n' % (index + 1, balance, 0)

if __name__ == '__main__':
	balance = float(raw_input('Enter opening balance:'))
	mon_pay = float(raw_input('Enter monthly payment:'))
	Payment(balance, mon_pay)