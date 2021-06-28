#!/usr/bin/env python3

"""
Ian 2020-01-10
add flags to clips, I guess
"""

import ResolveLib.ianresolvelib as r

folderList = []

def main():
	def recurse(folder):
		for f in folder.GetClipList():
			
			fp = f.GetClipProperty('File Path')

			if (fp):
				f.ClearFlags('All')
				# print(fp)

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
