#!/usr/bin/env python3

import os
import argparse
import ResolveLib.ianresolvelib as resolve

renderPreset = "MP4 1080p"

parser = argparse.ArgumentParser(description="Add timelines to Resolve's render queue by specifying a suffix.")
parser.add_argument("-d", "--dest", help="Destination directory for the renders")
parser.add_argument("-k", "--keep", help="Keep the queue instead of deleting it")
parser.add_argument("-p", "--preset", help="Override the default preset")
parser.add_argument("regexp")
args = parser.parse_args()

# print(args.dest)
if not args.dest:
    args.dest = os.getcwd()

if args.preset:
    renderPreset = args.preset

if not args.keep:
    resolve.DeleteAllRenderJobs()

for tl in resolve.GetTimelinesByRegexp(args.regexp):
    resolve.AddTimelineToRender(tl, renderPreset, args.dest)