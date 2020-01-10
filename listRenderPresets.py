#!/usr/bin/env python3

"""
Ian 2020-01-10
print out the timelines that end with a certain string in json format
"""

from ResolveLib.python_get_resolve import GetResolve
import json
import sys
import argparse


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
