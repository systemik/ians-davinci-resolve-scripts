#!/usr/bin/env python3

import json

def main():
    """
    list all the folders and projects from the root folder in resolve
    """
    import ResolveLib.ianresolvelib as r
    
    root = {}
    
    def listProjects(folder=None):
        thisFolder = {}
        if folder is not None:
            r.projectManager.OpenFolder(folder)
            print(f'In the folder {folder}, I found the following folders')
            thisFolder["folder"] = folder
        else:
            thisFolder["folder"] = "root"


        for currentFolder in r.projectManager.GetFolderListInCurrentFolder():
            print(currentFolder)
            listProjects(currentFolder)
        
        
        thisFolder["projects"] = r.projectManager.GetProjectsInCurrentFolder()
        r.projectManager.GotoParentFolder()
        
        root[folder] = thisFolder
        
        return


    r.projectManager.GotoRootFolder()
    
    listProjects()
    # print(r.projectManager.GetProjectsInCurrentFolder())

    # for currentFolder in r.projectManager.GetFolderListInCurrentFolder():
        # listProjects(currentFolder)
        
    # root["projects"] = r.projectManager.GetProjectsInCurrentFolder()
    
    # r.projectManager.OpenFolder("_archive")
    
    # root["_archive"] = r.projectManager.GetProjectsInCurrentFolder()
    
    print(json.dumps(root))

if __name__ == "__main__":
    main()