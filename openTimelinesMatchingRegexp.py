import ResolveLib.ianresolvelib as r
import argparse

parser = argparse.ArgumentParser(description="Like it says on the tin")

parser.add_argument("regexp", help="Regular expression to match against timeline names")

args = parser.parse_args()

x = r.GetTimelinesByRegexp(args.regexp)
# x = r.GetTimelineNameAndIndexBySuffix('06')
for f in x:
    r.project.SetCurrentTimeline(f)
# r.project.SetCurrentTimeline(tlObj)