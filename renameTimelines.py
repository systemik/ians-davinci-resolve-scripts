#!/usr/bin/env python3

# import os
import argparse
import ResolveLib.ianresolvelib as resolve
import re

parser = argparse.ArgumentParser(description="Rename Resolve timelines by specifying a regular expression.")
parser.add_argument("search", help="Search term, adoy")
parser.add_argument("replace", help="Replace term innit")
parser.add_argument("-q", "--quiet", action="store_true", help="Ssshhhh")
# parser.add_argument("-t", "--test", help="Check out what will happen before doing it")
args = parser.parse_args()

p = re.compile(args.search)
for tl in resolve.GetTimelinesByRegexp(args.search):
    # resolve.AddTimelineToRender(tl, renderPreset, args.dest)

    tlName = tl.GetName()
    x = p.sub(args.replace, tlName)
    if not args.quiet:
        print(f'{tlName} > {x}')
    tl.SetName(x)