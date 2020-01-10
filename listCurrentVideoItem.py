#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

item = r.project.GetCurrentTimeline().GetCurrentVideoItem()
print(item.GetName())

print(item)
