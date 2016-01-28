#!/usr/bin/env python
# -*- coding: utf-8 -*-


num = range(21)

alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
'eighteen', 'nighteen', 'twenty']

par_num = {30:'thirty', 40:'forty', 50:'fifteen',
60:'sixty', 70:'senenty', 80:'eighty', 90:'ninety',
1000:'one thousand'}

num_dict = dict(zip(num, alpha))
num_dict.update(par_num)

def judge_num(number):

	num_len = len(number)

	try:
		return num_dict[int(number)]
	except KeyError:
		if num_len == 2:
			fact_num = num_dict[int(number[0] + '0')] + '-' + \
			num_dict[int(number[1])]

		elif num_len == 3 and number[1:3] == '00':
			fact_num = num_dict[int(number[0])] + ' hundred'

		elif num_len == 3 :
			fact_num = num_dict[int(number[0])] + ' hundred and ' +\
			num_dict[int(number[1] + '0')] + '-' +\
			num_dict[int(number[2])]

		else:
			fact_num = '超出可访问范围！'

		return fact_num

if __name__ == '__main__':
	while 1:
		number = raw_input('Enter a number 0~1000:')
		print 'Converting...'
		print judge_num(number)
		print