#!/usr/bin/env python

import os
import argparse
import ResolveLib.ianresolvelib as resolve

# renderPreset = "MP4 1080p"

parser = argparse.ArgumentParser(description="Add timelines to Resolve's render queue by specifying a suffix.")
parser.add_argument("-c", "--clear", help="Clear render queue first", action="store_true")
parser.add_argument("-d", "--dest", help="Destination directory for the renders")
parser.add_argument("-p", "--preset", help="The name of the preset to be used")
parser.add_argument("suffix", help="The suffix to match against timeline names")
args = parser.parse_args()

# print(args.dest)
if not args.dest:
    args.dest = os.getcwd()

if not args.preset:
    args.preset = resolve.renderPreset

if args.clear:
    resolve.DeleteAllRenderJobs()

for tl in resolve.GetTimelinesBySuffix(args.suffix):
    resolve.AddTimelineToRender(tl, args.preset, args.dest)