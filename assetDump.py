#!/usr/bin/env python3

"""
Ian 2020-01-10
print full path names for all assets that have 'em
ianhaigh.com
"""

import ResolveLib.ianresolvelib as r
# import json
# import sys
# import argparse

# parser = argparse.ArgumentParser(description="List all the timelines in the currently opened Resolve project.")
# parser.add_argument("-j", "--json", help="Output in JSON format.", action="store_true")

# args = parser.parse_args()

# why do I have to add 1? Who knows?
# timelineCount = int(r.project.GetTimelineCount() + 1)

folderList = []

def main():
	def recurse(folder):
		for f in folder.GetClipList():
			
			fp = f.GetClipProperty('File Path')
			if (fp):
				print(fp)

		for fol in folder.GetSubFolderList():
			fname = r.bcolors.OKGREEN + fol.GetName() + r.bcolors.ENDC
			folderList.append(fname)
			print("/".join(folderList))
			recurse(fol)
			folderList.pop()

	root = r.project.GetMediaPool().GetRootFolder()
	folderList.append(root.GetName())
	recurse(root)
	# for f in (root.GetClipList()):
		# print(f.GetName())
	# for f in (root.GetSubFolderList()):
	# 	print(f.GetName())

if __name__ == "__main__":
	main()
