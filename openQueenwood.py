#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r
import argparse

""" 
Open the most recent version of a project.

Pass in the "top level" folder name, and it assumes that there are loads of 
files there named "Project 01" "Project 02" et cetera. Manual versioning.

This script lists them in alphabetical order and then opens the last  
one in the list. So … hopefully it works for you? No guarantees.
"""

parser = argparse.ArgumentParser(description="Open the last (hopefully most recent) version of a file in a folder, in Resolve.")
parser.add_argument("folder_name", help="The name of the folder to look in.")
args = parser.parse_args()

topLevelFolderName = args.folder_name

r.bringToFront()

r.projectManager.GotoRootFolder()
r.projectManager.OpenFolder(topLevelFolderName)

projects = r.projectManager.GetProjectsInCurrentFolder()

print(projects)

# can't access a dict by index, apparently. Coerce to a list first
# lastOne = list(projects.values())[-1]

# r.projectManager.LoadProject(lastOne)
