#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

tl = r.project.GetCurrentTimeline()

print(f'Current Timeline: {tl.GetName()}')

mediaPool = r.project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
subFolders = rootFolder.GetSubFolderList()

currentFolder = mediaPool.GetCurrentFolder()
print(currentFolder.GetName())


# Chose TimeLine and put time to 0

y = r.GetTimelinesByRegexp('^PH')
for g in y:
    print(f"Timeline '{g.GetName()}'")
    r.project.SetCurrentTimeline(g)
    tl.SetCurrentTimecode('00:00:00:00')
    tl.AddTrack('video')
    tl.DeleteTrack('video',0)
    tl.DeleteTrack('video',1)
    tl.DeleteTrack('video',2)

