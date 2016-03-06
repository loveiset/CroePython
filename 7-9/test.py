#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tr(srcstr, dststr, string):
	str_dict = dict(zip(srcstr.lower(), dststr))
	remain = srcstr[len(dststr):]
	new_strdict = []
	for i in string:
		if i in remain:
			continue
		if str_dict.get(i, 1) == 1:
			new_strdict.append(i)
		else:
			new_strdict.append(str_dict.get(i))
	new_str = ''.join(new_strdict)
	return new_str


