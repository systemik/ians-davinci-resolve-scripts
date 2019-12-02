import ResolveLib.ianresolvelib as r
import subprocess

# x = r.GetTimelinesByRegexp('06$')
x = r.GetTimelineNameAndIndexBySuffix('06')

# print(x)
timelineNames = []
for timeline in x:
    timelineNames.append(timeline['name'])

list = subprocess.Popen(('echo', "\n".join(timelineNames)), stdout=subprocess.PIPE)
output = subprocess.check_output(['fzf'], stdin=list.stdout, universal_newlines=True)
# nb I had to add universal_newlines so that it would return a string instead of a byte-object

list.wait()

answer = output.rstrip()
# print(timelineNames)
# print(timelineNames.index(answer))
indexToOpen = 0
for timeline in x:
    if timeline['name'] == answer:
        print(timeline['name'])
        indexToOpen = timeline['index']
        break

tlObj = r.project.GetTimelineByIndex(indexToOpen)
r.project.SetCurrentTimeline(tlObj)
# print(x)


# r.project.SetCurrentTimeline(x[2])
# subprocess.run(["fzf"])