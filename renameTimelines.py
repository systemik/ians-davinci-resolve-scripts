#!/usr/bin/env python3

""" 
Ian 2020-01-15
Rename timelines in DaVinci Resolve using regular expressions.
ianhaigh.com
"""
import argparse
import ResolveLib.ianresolvelib as resolve
import re

parser = argparse.ArgumentParser(description="Rename Resolve timelines by specifying a regular expression.")
parser.add_argument("search", help="Search term, adoy")
parser.add_argument("replace", help="Replace term innit")
parser.add_argument("-t", "--test", action="store_true", help="Don't do anything, just show what would happen")
parser.add_argument("-q", "--quiet", action="store_true", help="Ssshhhh")
parser.add_argument("-o", "--onlyin", help="Only rename timelines matching this regexp")
# parser.add_argument("-t", "--test", help="Check out what will happen before doing it")
args = parser.parse_args()

p = re.compile(args.search)

# figure out which timelines to match, first
if args.onlyin:
    timelines_to_rename = resolve.GetTimelinesByRegexp(args.onlyin)
else:
    timelines_to_rename = resolve.GetAllTimelines()

for tl in timelines_to_rename:

    tlName = tl.GetName()
    x = p.sub(args.replace, tlName)
    if not args.quiet:
        colourX = resolve.bcolors.OKGREEN + x + resolve.bcolors.ENDC
        print(f'{tlName}\n{colourX}\n')
    if not args.test:
        tl.SetName(x)