#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

""" open the most recent version of a project I'm working on """

topLevelFolderName = "Queenwood"

r.projectManager.GotoRootFolder()
r.projectManager.OpenFolder(topLevelFolderName)

projects = r.projectManager.GetProjectsInCurrentFolder()

# can't access a dict by index, apparently. Coerce to a list first
lastOne = list(projects.values())[-1]

r.projectManager.LoadProject(lastOne)