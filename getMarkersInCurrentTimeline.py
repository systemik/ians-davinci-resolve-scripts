#!/usr/bin/env python3

"""
Ian 2020-05-07
ianhaigh.com
"""

import ResolveLib.ianresolvelib as r
from timecode import Timecode

import json
import sys
import argparse

parser = argparse.ArgumentParser(description="List all the markers in the active timeline.")
# parser.add_argument("-j", "--json", help="Output in JSON format.", action="store_true")

args = parser.parse_args()

# why do I have to add 1? Who knows?
# timelineCount = int(r.project.GetTimelineCount() + 1)

tl = r.project.GetCurrentTimeline()
markers = tl.GetMarkers()

for f in markers.items():
	tc = Timecode(30, frames=f[0])
	print(tc)
	print(f[1]["name"])

"""
print(json.dumps(markers))

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
"""