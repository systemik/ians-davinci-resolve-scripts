#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

tl = r.project.GetCurrentTimeline()
print(f'Timeline: {tl.GetName()}')
markers = tl.GetMarkers()

item = r.project.GetCurrentTimeline().GetCurrentVideoItem()
print(item.GetName())

print(item)
