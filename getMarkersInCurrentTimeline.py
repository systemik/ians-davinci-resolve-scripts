#!/usr/bin/env python3

"""
Ian 
2020-05-07
initial

2021-08-30
commented code! plus don't bake in the frame rate (naughty)

ianhaigh.com
"""

import ResolveLib.ianresolvelib as r
from timecode import Timecode
import argparse

parser = argparse.ArgumentParser(description="List all the markers in the active timeline.")
# parser.add_argument("-j", "--json", help="Output in JSON format.", action="store_true")

args = parser.parse_args()

tl = r.project.GetCurrentTimeline()
framerate = float(tl.GetSetting("timelineFrameRate"))

# returns a dict with (frameId -> {information})
markers = tl.GetMarkers()

markerResult = []
for f in markers.items():
	currentMarker = ""
	# convert the framenumber to timecode, so it's easier to read
	tc = Timecode(framerate, frames=f[0])
	# currentMarker["tc"] = tc
	# currentMarker["name"] = f[1]["name"]

	currentMarker = str(tc) + "\n"
	currentMarker = currentMarker + f[1]["name"]

	markerResult.append(currentMarker)

print("\n\n".join(markerResult))


# this one is quite cool too
# print("\n".join(map(str, markerResult)))

# below here? um … just old stuff that I can't bring myself to throw out, I guess

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
