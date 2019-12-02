#!/usr/bin/env python

"""
Ian 2019-10-08
print out the timelines that end with a certain string in json format
"""

from python_get_resolve import GetResolve
import json
import sys

def DisplayTimelinesInfo( project ):
	timelineCount = project.GetTimelineCount()

	obj = []
	for index in range (0, int(timelineCount)):
		tmp={}

		updatedIndex = index + 1
		timelineName = project.GetTimelineByIndex(updatedIndex).GetName()
		
		tmp["name"] = timelineName
		tmp["index"] = updatedIndex
		obj.append(tmp)

	print(json.dumps(obj))
	return

resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

DisplayTimelinesInfo(project)
