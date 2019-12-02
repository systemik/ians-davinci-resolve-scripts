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

print(project.GetRenderFormats())

"""
{'JPEG 2000': 'j2c', 'QuickTime': 'mov', 'BRAW': 'braw', 'IMF': 'imf', 'MTS': 'mts', 'Panasonic AVC': 'pavc', 'MXF OP-Atom': 'mxf', 'DPX': 'dpx', 'MXF OP1A': 'mxf_op1a', 'MP4': 'mp4', 'EXR': 'exr', 'AVI': 'avi', 'MJ2': 'mj2', 'TIFF': 'tif', 'Wave': 'wav', 'DCP': 'dcp'}
"""