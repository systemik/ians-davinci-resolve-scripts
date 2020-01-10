#!/usr/bin/env python3

""" open every timeline in Resolve whose name matches a regular expression """
""" Updated 2020-01-10 """

import ResolveLib.ianresolvelib as r
import argparse

parser = argparse.ArgumentParser(description="Open every timeline in Resolve whose name matches a regular expression")

parser.add_argument("-q", "--quiet", help="Be quiet about it", action="store_true")
parser.add_argument("regexp", help="Regular expression to match against timeline names")

args = parser.parse_args()

x = r.GetTimelinesByRegexp(args.regexp)
for f in x:
    if not args.quiet:
        print(f"Opening '{f.GetName()}'")
    r.project.SetCurrentTimeline(f)