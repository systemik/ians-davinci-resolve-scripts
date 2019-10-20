from ianresolve import GetResolve

resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

print(projectManager.GetProjectsInCurrentFolder())