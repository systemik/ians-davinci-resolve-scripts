#!/usr/bin/env python3

"""
Ian 2021-06-28
add flags to clips based on the camera number
"""

import ResolveLib.ianresolvelib as r

def main():
	def recurse(folder):
		for f in folder.GetClipList():
		# loop through every clip in this folder
			
			if (f.GetClipProperty("Camera #") == "1"):
				f.AddFlag("Yellow")
			elif (f.GetClipProperty("Camera #") == "2"):
				f.AddFlag("Cyan")
			else:
				# if it doesn't have camera 1 or 2, just clear the flags
				f.ClearFlags("All")

		for fol in folder.GetSubFolderList():
			# call this function for each subfolder we find
			recurse(fol)

	# get the root folder of the whole media pool
	root = r.project.GetMediaPool().GetRootFolder()
	# start the recursion
	recurse(root)

if __name__ == "__main__":
	# start here
	main()
