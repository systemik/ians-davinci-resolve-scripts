import ianresolve
import sys

from ianresolve import GetResolve

resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

if len(sys.argv) < 2:
    print("lemme know what to search for")
    sys.exit()

searchTerm = sys.argv[1]

ianresolve.DisplayTimelinesInfo(project, searchTerm)