#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

item = r.project.GetCurrentTimeline().GetCurrentVideoItem()
print(item.GetName())

mpi = item.GetMediaPoolItem()
print(mpi.GetClipProperty('FPS'))

mpi.SetClipProperty('FPS', '23.976')

print(mpi.GetClipProperty('FPS'))
# GetClipProperty
