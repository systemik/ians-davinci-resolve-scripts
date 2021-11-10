#!/usr/bin/env python -Wignore

"""
Ian 2020-10-20
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
    description="Add timelines to Resolve render queue.")

parser.add_argument(
    "-k", "--keep", help="Keep the queue instead of clearing it first",
    action="store_true")

parser.add_argument(
    "-s", "--start", help="Start rendering immediately",
    action="store_true")

# parser.add_argument(
#     "-r", "--regexp", help="Interpret as regular expression"
# )

parser.add_argument(
    "-d", "--dest", help="Destination directory for the renders")

parser.add_argument(
    "-p", "--preset", help="Rendering preset to use")

parser.add_argument(
    '-r', '--regexp', help="Interpret as regular expression")

parser.add_argument(
    'timelines', nargs=argparse.REMAINDER
)

args = parser.parse_args()

if not args.dest:
    args.dest = pathToRenders()
    # print(args.dest)
    # args.dest = os.getcwd()

renderPreset = ""
print(args)
if args.preset:
    renderPreset = args.preset

if not args.keep:
    resolve.DeleteAllRenderJobs()

if args.regexp:
    for tl in resolve.GetTimelinesByRegexp(args.regexp):
        resolve.AddTimelineToRender(tl, renderPreset, args.dest)
else:
    # set1 = set(args.timelines)
    # set2 = set(resolve.GetTimelineNamesAsList())
    for tl in resolve.GetAllTimelines():
        if (tl.GetName() in args.timelines):
            print(renderPreset)
            resolve.AddTimelineToRender(tl, renderPreset, args.dest)


if args.start:
    resolve.project.StartRendering()
