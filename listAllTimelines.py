#!/usr/bin/env python3

"""
Ian 2020-01-10
print out the timelines that end with a certain string in json format
"""

import ResolveLib.ianresolvelib as r
import json
import sys
import argparse

parser = argparse.ArgumentParser(description="List all the timelines in the currently opened Resolve project.")
parser.add_argument("-j", "--json", help="Output in JSON format.", action="store_true")

args = parser.parse_args()

# why do I have to add 1? Who knows?
timelineCount = int(r.project.GetTimelineCount() + 1)

def DisplayTimelinesJSON( project ):

	obj = []
	for index in range (1, timelineCount):
		tmp={}

		# updatedIndex = index + 1
		timeline = project.GetTimelineByIndex(index)
		# timelineName = project.GetTimelineByIndex(updatedIndex).GetName()
		
		tmp["name"] = timeline.GetName()
		# tmp["index"] = updatedIndex
		tmp["index"] = index
		obj.append(tmp)

	print(json.dumps(obj))
	return

if args.json:
	DisplayTimelinesJSON(r.project)
else:
	for index in range(1, timelineCount):
		timeline = r.project.GetTimelineByIndex(index)
		print(timeline.GetName())
