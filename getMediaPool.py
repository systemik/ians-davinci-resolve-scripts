#!/usr/bin/env python3 -Wignore

"""
Ian 2020-01-15
What's in that doggone media pool anyway
ianhaigh.com
"""

import ResolveLib.ianresolvelib as r
import json

mp = r.project.GetMediaPool()
# x = (tl.GetSetting())

root = mp.GetRootFolder()

# clipList = root.GetClipList()

subbies = root.GetSubFolderList()


i = {}

for i in subbies:
	# print(i.GetName())
	# print(i.GetClipProperty())
	if ("MC" in i.GetName()):
		print("bingo")
		mp.SetCurrentFolder(i)

		break





# print(r.project.GetName())

# print(json.dumps(tl))
