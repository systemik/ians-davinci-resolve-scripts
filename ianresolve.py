#!/usr/bin/env python

"""
Ian's Library of Resolve things, deprecated in favour of ianresolvelib
"""

import json
import sys

def GetResolve():
	import imp
	expectedPath="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/"
	bmd = imp.load_source('DaVinciResolveScript', expectedPath+"DaVinciResolveScript.py")

	try:
	# The PYTHONPATH needs to be set correctly for this import statement to work.
	# An alternative is to import the DaVinciResolveScript by specifying absolute path (see ExceptionHandler logic)
		import DaVinciResolveScript as bmd
	except ImportError:
		if sys.platform.startswith("darwin"):
			expectedPath="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/"
		elif sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
			import os
			expectedPath=os.getenv('PROGRAMDATA') + "\\Blackmagic Design\\DaVinci Resolve\\Support\\Developer\\Scripting\\Modules\\"
		elif sys.platform.startswith("linux"):
			expectedPath="/opt/resolve/libs/Fusion/Modules/"
		
		# check if the default path has it...
		# print("Unable to find module DaVinciResolveScript from $PYTHONPATH - trying default locations")
		try:
			import imp
			bmd = imp.load_source('DaVinciResolveScript', expectedPath+"DaVinciResolveScript.py")
		except ImportError:
			# No fallbacks ... report error:
			print("Unable to find module DaVinciResolveScript - please ensure that the module DaVinciResolveScript is discoverable by python")
			print("For a default DaVinci Resolve installation, the module is expected to be located in: "+expectedPath)
			sys.exit()
	
	return bmd.scriptapp("Resolve")

def ListAllTimelines(arg):
    pass

def DisplayTimelinesInfo( project, searchTerm ):
    timelineCount = project.GetTimelineCount()

    obj = []
    for index in range (0, int(timelineCount)):
        tmp={}

        updatedIndex = index + 1
        timelineName = project.GetTimelineByIndex(updatedIndex).GetName()
        
        if timelineName.endswith(searchTerm):
            tmp["name"] = timelineName
            tmp["index"] = updatedIndex
            obj.append(tmp)

    print(json.dumps(obj))
    return

if __name__ == "__main__":
    pass
    # DisplayTimelinesInfo(project, searchTerm)
