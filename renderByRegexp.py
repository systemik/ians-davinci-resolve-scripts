#!/usr/bin/env python3 -Wignore

"""
Ian 2020-01-15
Pass this script a regular expression (e.g. '24$' to render every timeline)
that ends in '24') and this script will put each match into the render queue.
ianhaigh.com
"""


import argparse
import ResolveLib.ianresolvelib as resolve


def pathToRenders():
    # my super specific bit that uses the ketchup-projects
    # project to find the right flodder
    import json

    CONFIG = "/Users/ian/.ketchupProjects.json"
    configJSON = json.load(open(CONFIG))
    return configJSON["currentProject"] + "/support/9_renders/preview_renders"


# set a default here if you prefer not to use an option each time
renderPreset = "MP4 1080p"

parser = argparse.ArgumentParser(
    description="Add timelines to Resolve render queue by regexp.")

parser.add_argument(
    "-k", "--keep", help="Keep the queue instead of clearing it first",
    action="store_true")

parser.add_argument(
    "-s", "--start", help="Start rendering immediately",
    action="store_true")

parser.add_argument(
    "-d", "--dest", help="Destination directory for the renders")

parser.add_argument("-p", "--preset", help="Rendering preset to use")
parser.add_argument("regexp")
args = parser.parse_args()

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

if args.start:
    resolve.project.StartRendering()
