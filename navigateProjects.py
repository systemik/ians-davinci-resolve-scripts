#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r
from subprocess import Popen, PIPE, call

CHOOSE = '/usr/local/bin/choose'

r.projectManager.GotoRootFolder()
# print(r.projectManager.GetProjectsInCurrentFolder())
folders = (r.projectManager.GetFoldersInCurrentFolder())
topFolders = []
[topFolders.append(value) for (key, value) in folders.items()]

print(f'topFolders: {topFolders}')
p1 = Popen(["echo", topFolders], stdout=PIPE)
p2 = Popen([CHOOSE, "-c", "", "-f", "Inconsolata"],
           stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
# decode gets rid of the annoying b'' prefix
output = p2.communicate()[0].decode()
