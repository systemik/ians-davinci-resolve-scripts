from python_get_resolve import GetResolve
import json
import sys
import re
# import config

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

renderFormat = 'mov'
renderCodec = 'Apple ProRes 422 HQ'
renderPreset = 'MP4 1080p'
renderPath = '/Users/ian/Desktop'
renderPresetName = 'ProRes Master'

def GetTimelinesByRegexp(regexp):
    """return array of timelines matching a regexp"""
    timelineCount = project.GetTimelineCount()
    # compiled = re.compile(regexp)

    obj = []
    for index in range(0, int(timelineCount)):
        updatedIndex = index + 1
        timeline = project.GetTimelineByIndex(updatedIndex)
        timelineName = timeline.GetName()

        # print(timelineName)
        m = re.search(regexp, timelineName)
        if m:
            obj.append(timeline)

    return(obj)

def GetTimelinesBySuffix(suffix):
    """return array of timelines with a certain suffix"""
    timelineCount = project.GetTimelineCount()

    obj = []
    for index in range(0, int(timelineCount)):
        updatedIndex = index + 1
        timeline = project.GetTimelineByIndex(updatedIndex)
        timelineName = timeline.GetName()

        if timelineName.endswith(suffix):
            obj.append(timeline)

    return(obj)

def GetTimelineNameAndIndexBySuffix(suffix):
    """return array of timelines with a certain suffix"""
    timelineCount = project.GetTimelineCount()

    obj = []
    for index in range(0, int(timelineCount)):
        tmp = {}

        updatedIndex = index + 1
        timelineName = project.GetTimelineByIndex(updatedIndex).GetName()

        if timelineName.endswith(suffix):
            tmp["name"] = timelineName
            tmp["index"] = updatedIndex
            obj.append(tmp)
    return(obj)

def GetAllTimelineNameAndIndices():
    """return array of timelines objects with name and index properties"""
    timelineCount = project.GetTimelineCount()

    obj = []
    for index in range(0, int(timelineCount)):
        tmp = {}

        updatedIndex = index + 1
        timelineName = project.GetTimelineByIndex(updatedIndex).GetName()

        tmp["name"] = timelineName
        tmp["index"] = updatedIndex
        obj.append(tmp)
    return(obj)

def GetAllTimelines():
    """return all timelines"""
    timelineCount = project.GetTimelineCount()

    obj = []
    for index in range(0, int(timelineCount)):
        updatedIndex = index + 1
        timeline = project.GetTimelineByIndex(updatedIndex)
        obj.append(timeline)
    return(obj)

def PrettyPrintTimelinesWithSuffix(suffix):
    timelines = GetTimelinesBySuffix(suffix)
    for t in timelines:
        print(t.GetName())

def PrettyPrintAllTimelines():
    timelines = GetAllTimelines()
    for t in timelines:
        print(t.GetName())

def DeleteAllRenderJobs():
    project.DeleteAllRenderJobs()
    return

def RenderWithMarkOut( timeline, presetName, targetDirectory, out=0):
    project.SetCurrentTimeline(timeline)
    # startFrame = timeline.GetStartFrame()
    project.SetRenderSettings({"SelectAllFrames" : 0, "TargetDir" : targetDirectory, "MarkIn": 0, "MarkOut" : 500})
    project.LoadRenderPreset(presetName)
    return project.AddRenderJob()

def AddTimelineToRender( timeline, presetName, targetDirectory, out=0):
    project.SetCurrentTimeline(timeline)
    project.LoadRenderPreset(presetName)
    startFrame = timeline.GetStartFrame()

    # if not project.SetCurrentRenderFormatAndCodec(renderFormat, renderCodec):
    # 	return False
    print(f"hey render: {out}")
    if out is not 0:
        print(f"rendering {out}")
        project.SetRenderSettings({"SelectAllFrames" : 0, "TargetDir" : targetDirectory, "MarkIn": startFrame, "MarkOut" : startFrame + out})
    else:
        project.SetRenderSettings({"SelectAllFrames" : 1, "TargetDir" : targetDirectory})

    print(f"Added {timeline.GetName()}")
    return project.AddRenderJob()

def GetProjectsInCurrentFolder():
    return projectManager.GetProjectsInCurrentFolder()

def GreenHeading(s):
    return bcolors.OKGREEN + f"{s}\n" + bcolors.ENDC

def Indent(s):
    return f"\t{s}\n"

def InfoProjects():
    """return a string of projects in current folder"""
    s = GreenHeading("GetProjectsInCurrentFolder")
    projs = projectManager.GetProjectsInCurrentFolder()
    for key, value in projs.items():
        s += Indent(value)
    return s

def InfoRenderFormats():
    """return a string of render formats"""
    s = GreenHeading("GetRenderFormats")
    for key, value in project.GetRenderFormats().items():
        s += Indent(value)
    return s

def InfoRenderPresets():
    """return a string of render presets"""
    s = GreenHeading("GetRenderPresets")
    for key, value in project.GetRenderPresets().items():
        s += Indent(value)
    return s

def GetLotsOfInfo():
    """print a bunch of useful stuff"""
    s = ""
    s += InfoProjects()
    s += InfoRenderFormats()
    s += InfoRenderPresets()
    return s

def bringToFront():
    import subprocess
    # from subprocess import run
    subprocess.run(['open', '-a', "Davinci Resolve"])
    
if __name__ == "__main__":
    # DeleteAllRenderJobs()
    # for tl in GetTimelinesBySuffix("06"):
        # AddTimelineToRender(tl, renderPreset, renderPath)
    
    print(GetTimelinesByRegexp(sys.argv[1:]))

