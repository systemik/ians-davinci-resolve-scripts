#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

tl = r.project.GetCurrentTimeline()
# print(f'Timeline: {tl.GetName()}')
# markers = tl.GetMarkers()

items = r.project.GetCurrentTimeline().GetItemListInTrack("video", 3)
for current in items:
	name = current.GetName()
	duration = current.GetDuration()

	print(f"{name}, {duration}")


	



# print(item)
