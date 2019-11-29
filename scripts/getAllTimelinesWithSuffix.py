#!/usr/bin/env python

import sys

from ianresolvelib import *

if len(sys.argv) < 2:
	print("lemme know what to search for")
	sys.exit()

searchTerm = sys.argv[1]

# print(getTimelineNameAndIndexBySuffix(searchTerm))
print(getTimelinesBySuffix("06"))
