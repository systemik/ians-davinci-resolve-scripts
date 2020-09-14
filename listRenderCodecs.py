#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

print(r.project.GetRenderCodecs('mov'))

"""
example output

{'JPEG 2000': 'j2c', 'QuickTime': 'mov', 'BRAW': 'braw', 'IMF': 'imf', 'MTS': 'mts', 'Panasonic AVC': 'pavc', 'MXF OP-Atom': 'mxf', 'DPX': 'dpx', 'MXF OP1A': 'mxf_op1a', 'MP4': 'mp4', 'EXR': 'exr', 'AVI': 'avi', 'MJ2': 'mj2', 'TIFF': 'tif', 'Wave': 'wav', 'DCP': 'dcp'}
"""