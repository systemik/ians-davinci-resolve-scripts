#!/usr/bin/env python

from python_get_resolve import GetResolve
import sys
import time

def AddTimelineToRender( project, timeline, presetName, targetDirectory:"/Volumes/22-ketchup/work/QWND001 Values/support/9_renders/preview_renders/v03", renderFormat, renderCodec ):
	project.SetCurrentTimeline(timeline)
	# project.LoadRenderPreset(presetName)
	
	# if not project.SetCurrentRenderFormatAndCodec(renderFormat, renderCodec):
	# 	return False
	
	project.SetRenderSettings({"SelectAllFrames" : 1, "TargetDir" : targetDirectory})
	print(f"Added {timeline.GetName()}")
	return project.AddRenderJob()

def RenderAllTimelines( resolve, presetName, targetDirectory, renderFormat, renderCodec ):
	projectManager = resolve.GetProjectManager()
	project = projectManager.GetCurrentProject()
	if not project:
		return False
	
	resolve.OpenPage("Deliver")
	timelineCount = project.GetTimelineCount()
	
	for index in range (0, int(timelineCount)):
		if not AddTimelineToRender(project, project.GetTimelineByIndex(index + 1), presetName, targetDirectory, renderFormat, renderCodec):
			print("failed at line 34")
			return False
	return project.StartRendering()

def IsRenderingInProgress( resolve ):
	projectManager = resolve.GetProjectManager()
	project = projectManager.GetCurrentProject()
	if not project:
		return False
		
	return project.IsRenderingInProgress()

def WaitForRenderingCompletion( resolve ):
	while IsRenderingInProgress(resolve):
		time.sleep(1)
	return

def DeleteAllRenderJobs( resolve ):
	projectManager = resolve.GetProjectManager()
	project = projectManager.GetCurrentProject()
	project.DeleteAllRenderJobs()
	return

# Inputs: 
# - DRX file to import grade still and apply it for clips
# - grade mode (0, 1 or 2)
# - preset name for rendering
# - render path
# - render format
# - render codec
# if len(sys.argv) < 7:
# 	print("input parameters for scripts are [drx file path] [grade mode] [render preset name] [render path] [render format] [render codec]")
# 	sys.exit()

# drxPath = sys.argv[1]
# gradeMode = sys.argv[2]
# renderPresetName = sys.argv[3]
# renderPath = sys.argv[4]
# renderFormat = sys.argv[5]
# renderCodec = sys.argv[6]

renderFormat = 'mov'
renderCodec = 'Apple ProRes 422 HQ'
renderPath = '/Users/ian/Dropbox (Ketchup)/work/BES039 Asia Videos/support/9_renders/preview_renders'
renderPresetName = 'ProRes Master'
# Get currently open project
resolve = GetResolve()

# if not ApplyDRXToAllTimelines(resolve, drxPath, gradeMode):
# 	print("Unable to apply a still from drx file to all timelines")
# 	sys.exit()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
project.LoadRenderPreset('MP4 1080p')


if not RenderAllTimelines(resolve, renderPresetName, renderPath, renderFormat, renderCodec):
	print("Unable to set all timelines for rendering")
	sys.exit()


WaitForRenderingCompletion(resolve)

# DeleteAllRenderJobs(resolve)

print("Rendering is completed.")
