#!/usr/bin/env python

import ianresolvelib as resolve

resolve.DeleteAllRenderJobs()

for tl in resolve.GetTimelinesBySuffix("06"):
    resolve.AddTimelineToRender(tl, "MP4 1080p", "/Volumes/22-ketchup/work/QWND001 Values/support/9_renders/preview_renders/v06")

# print(project.GetRenderFormats())
