#!/usr/bin/env python3

import json


def main():
    """
    Recursively list all the folders and
    projects from the root folder in resolve.
    Dumps everything to json.
    """
    import ResolveLib.ianresolvelib as r

    root = {}
    r.projectManager.GotoRootFolder()

    def listProjects(folder=None, parentObj=None):
        """
        Oh my god I think my recursion thing works!
        This loops thru all the folders and builds an object 
        that reflects the project manager's contents
        """
        # make a new obj to store all of this folder's properties
        currentFolderObj = {}

        if folder is not None:
            # descend into the relevant folder
            r.projectManager.OpenFolder(folder)
        else:
            # we're being called for the first time
            folder = "root"

        # where the magic – ahem – where the recursion happens
        for currentFolder in r.projectManager.GetFolderListInCurrentFolder():
            listProjects(
                folder=currentFolder, parentObj=currentFolderObj)

        # put the project dict onto a property called "projects"
        currentFolderObj["projects"] = r.projectManager.GetProjectsInCurrentFolder()

        # attach the currentFolderObj to the parent object
        if parentObj is not None:
            parentObj[folder] = currentFolderObj

        # unwind the recursion
        r.projectManager.GotoParentFolder()

        return

    listProjects(parentObj=root)
    print(json.dumps(root))


if __name__ == "__main__":
    main()
