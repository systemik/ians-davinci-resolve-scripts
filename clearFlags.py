#!/usr/bin/env python3

"""
Ian 2021-06-28
demolish all the flags on all the clips
"""

import ResolveLib.ianresolvelib as r

def main():
	def recurse(folder):
		for f in folder.GetClipList():
			f.ClearFlags('All')

		for fol in folder.GetSubFolderList():
			recurse(fol)

	root = r.project.GetMediaPool().GetRootFolder()
	recurse(root)

if __name__ == "__main__":
	main()
