from python_get_resolve import GetResolve
import json
import sys


resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

def getTimelinesBySuffix(suffix):
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

def getTimelineNameAndIndexBySuffix(suffix):
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



def getAllTimelines():
    """return all timelines"""
    timelineCount = project.GetTimelineCount()

    obj = []
    for index in range(0, int(timelineCount)):
        updatedIndex = index + 1
        timeline = project.GetTimelineByIndex(updatedIndex)
        obj.append(timeline)
    return(obj)


if __name__ == "__main__":
    pass
