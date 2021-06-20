#!/usr/bin/env python

import pickle
import collections

with open('donotshare') as handle:
	o = pickle.load(handle)

outstr = ''
for line in o:
    for char,n in line:
        outstr += char*n
    outstr += '\n'
print outstr
