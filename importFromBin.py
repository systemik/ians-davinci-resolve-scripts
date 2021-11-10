#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    import ResolveLib.ianresolvelib as r

    mp = r.project.GetMediaPool()
    root = mp.GetRootFolder()

    currentFolder = mp.GetCurrentFolder()
    print(currentFolder.GetName())
