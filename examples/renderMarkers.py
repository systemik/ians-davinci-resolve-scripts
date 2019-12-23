#
# RenderMarkers - version: DR15.001.00 #490224.01 -- by Sam Cogheil (SimplSam)   
#
# Public Domain | No Warranty - Expressed or Implied
#

#
# This is a Black Magic Design "DaVinci Resolve" companion Python script
# Exports a set of frames from defined Marker positions
# 
# To use:
#   (1) - (Option) Update relevant entries in the PREFERENCES section
#   (2) - Run the file in Batch, DR Console or Fusion Menu etc. 
#
# Platforms/Tested:
#   DR15 Studio (Win10). No other platforms have been evaluated
#
import time
#----------------------------------------------------
#- PREFERENCES
#----------------------------------------------------
RENDER_QUEUE  = True #- [True|False] Render the jobs queue to output media?
DELETE_QUEUE  = True #- [True|False] Clear the render job queue before new jobs added?
RENDER_PRESET = ""   #- Preload base settings from Render Preset . i.e. "H.264 Master"
MARKER_MATCH  = ""   #- "Purple" only matches Purple markers. "" matches all

#-\ Use TARGET_DIR, FILE_NAME and FRAMES_SIZE with GUI Custom Filename setting:
TARGET_DIR    = "C:\\somevalidpath"  #- Directory Path. *Need* to escape backslashes
FILE_NAME     = ""   #- Custom Filename for output file(s)
FRAMES_SIZE   = 0    #- No. digits for Frame # appended to Filename. 0 = don't append

#---------------------------------------------------
#- RUN
#---------------------------------------------------
from python_get_resolve import GetResolve
resolve = GetResolve()
if (resolve):
  projectManager=resolve.GetProjectManager()
  if (projectManager):
    project=projectManager.GetCurrentProject()
    if (project):
      timeline=project.GetCurrentTimeline()
      if (timeline):
        if (DELETE_QUEUE): project.DeleteAllRenderJobs()
        if (RENDER_PRESET != ""): project.LoadRenderPreset(RENDER_PRESET)
        markers = timeline.GetMarkers()
        for markerFrame in markers.keys():
          markerFrame = markerFrame
          markerData = markers[markerFrame]
          if ((markerData["color"] == MARKER_MATCH) or (MARKER_MATCH == "")):
            print("Processing Marker at: " +  str(int(markerFrame)) + (" - " + str(int(markerData["duration"])) if (markerData["duration"]>1) else "") + " (" + markerData["name"] + ")")
            renderSettings = {}
            renderSettings["MarkIn"] = markerFrame
            renderSettings["MarkOut"] = markerFrame + int(markerData["duration"]) -1
            if (TARGET_DIR != ""): renderSettings["TargetDir"] = TARGET_DIR 
            fmtString = "%0" + str(FRAMES_SIZE) + "d"
            if (FILE_NAME != ""): renderSettings["CustomName"] = FILE_NAME + str((fmtString % markerFrame) if (FRAMES_SIZE>0) else "") 
            project.SetRenderSettings(renderSettings)   
            project.AddRenderJob()
        if (RENDER_QUEUE):
          project.StartRendering()   
          while (project.IsRenderingInProgress()):
            time.sleep(1)
      else: print("** Error: Timeline not open")
    else: print("** Error: Project not open")
  else: print("** Error: Project Manager not accessible")
else: print("** Error: Resolve not accessible")
print("--run done--")  