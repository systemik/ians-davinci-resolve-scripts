#!/usr/bin/env python3

""" What's the currently timecode on the current timeline? Currently? """

import ResolveLib.ianresolvelib as r

tl = r.project.GetCurrentTimeline()
print(tl.GetCurrentTimecode())
