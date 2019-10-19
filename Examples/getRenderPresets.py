#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Display project information: timeline, clips within timelines and media pool structure.
"""

from python_get_resolve import GetResolve

# Get currently open project
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

# DisplayProjectInfo(project)
# tl = project.GetCurrentTimeline()
# yay = (tl.GetCurrentVideoItem())

# print(yay)

print(project.GetRenderPresets())

"""
Example output
{1.0: 'YouTube - 720p', 2.0: 'YouTube - 1080p', 3.0: 'YouTube - 2160p', 4.0: 'Vimeo - 720p', 5.0: 'Vimeo - 1080p', 6.0: 'Vimeo - 2160p', 7.0: 'ProRes Master', 8.0: 'H.264 Master', 9.0: 'H.265 Master', 10.0: 'IMF - Generic', 11.0: 'IMF - 20th Century Fox', 12.0: 'IMF - Netflix', 13.0: 'Frame.io', 14.0: 'FCP - Final Cut Pro 7', 15.0: 'FCP - Final Cut Pro X', 16.0: 'Premiere XML', 17.0: 'AVID AAF', 18.0: 'Pro Tools', 19.0: 'Audio Only', 20.0: 'MXF ian', 21.0: '720p MP4', 22.0: 'AGSM b-roll', 23.0: 'amber subtitles', 24.0: 'Flight Centre wav', 25.0: 'Flight Centre for AE', 26.0: 'Flight Centre low res'}
"""