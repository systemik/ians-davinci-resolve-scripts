#!/usr/bin/env python

import os
import argparse
import ianresolvelib as resolve

renderPreset = "MP4 1080p"

parser = argparse.ArgumentParser(description="Add timelines to Resolve's render queue by specifying a suffix.")
parser.add_argument("-d", "--dest", help="Destination directory for the renders")
parser.add_argument("suffix")
args = parser.parse_args()

# print(args.dest)
if not args.dest:
    args.dest = os.getcwd()

resolve.DeleteAllRenderJobs()

for tl in resolve.GetTimelinesBySuffix(args.suffix):
    resolve.AddTimelineToRender(tl, renderPreset, args.dest)