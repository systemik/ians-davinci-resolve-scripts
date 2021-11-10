#!/usr/bin/env python3

"""
Ian 2020-01-15
What's the currently timecode on the current timeline? Currently?
ianhaigh.com
"""

import ResolveLib.ianresolvelib as r
import json

tl = r.project.GetCurrentTimeline()
x = (tl.GetSetting())


print(json.dumps(x))