#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = raw_input('a:')
b = raw_input('b:')
c = raw_input('c:')

L = []

if a>b:
	a, b = b, a

if a>c:
	a, c = c, a

if b>c:
	b, c = c, b

L.extend([a,b,c])

print L