#!/usr/bin/env python3

"""
Ian 2020-01-13
list all the render presets available
"""

import ResolveLib.ianresolvelib as r

print("\n".join(r.project.GetRenderPresets().values()))

""" 
Example output:

YouTube - 720p
YouTube - 1080p
YouTube - 2160p
Vimeo - 720p
Vimeo - 1080p
Vimeo - 2160p
ProRes Master
H.264 Master
H.265 Master
IMF - Generic
IMF - 20th Century Fox
IMF - Netflix
Frame.io
FCP - Final Cut Pro 7
FCP - Final Cut Pro X
Premiere XML
AVID AAF
Pro Tools
Audio Only
"""