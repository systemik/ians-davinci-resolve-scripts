#!/usr/bin/env python3

""" 
Ian 2020-01-15
Pass this script a regular expression (e.g. '24$' to render every timeline)
that ends in '24') and this script will put each match into the render queue.
ianhaigh.com
"""

import os
import argparse
import ResolveLib.ianresolvelib as resolve

def pathToRenders():
	import json

	CONFIG = "/Users/ian/.ketchupProjects.json"
	configJSON = json.load(open(CONFIG))
	return configJSON["currentProject"] + "/support/9_renders/preview_renders"
	
# set a default here if you prefer not to use an option each time
renderPreset = "MP4 1080p"

parser = argparse.ArgumentParser(description="Add timelines to Resolve's render queue by specifying a suffix.")
parser.add_argument("-k", "--keep", help="Keep the queue instead of clearing it first", action="store_true")
parser.add_argument("-d", "--dest", help="Destination directory for the renders")
parser.add_argument("-p", "--preset", help="Rendering preset to use")
parser.add_argument("regexp")
args = parser.parse_args()

print("hi there")
if not args.dest:
	args.dest = pathToRenders()
	print(args.dest)
	# args.dest = os.getcwd()

if args.preset:
	renderPreset = args.preset

if not args.keep:
	resolve.DeleteAllRenderJobs()

for tl in resolve.GetTimelinesByRegexp(args.regexp):
	resolve.AddTimelineToRender(tl, renderPreset, args.dest)

