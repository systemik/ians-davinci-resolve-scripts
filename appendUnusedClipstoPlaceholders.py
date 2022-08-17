#!/usr/bin/env python3

import ResolveLib.ianresolvelib as r

tl = r.project.GetCurrentTimeline()
#projectManager = r.projectManager.GetProjectManager()

print(f'Current Timeline: {tl.GetName()}')
#markers = tl.GetMarkers()

#item = r.project.GetCurrentTimeline().GetCurrentVideoItem()
#print(item.GetName())

#print(item)


mediaPool = r.project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
subFolders = rootFolder.GetSubFolderList()

currentFolder = mediaPool.GetCurrentFolder()
print(currentFolder.GetName())


#a print out of what subfolders are in the Master Folder

#print(mediaPool.OpenFolder(sub))
print ('These are the folders in the Master Folder:')


############################################################################################################
# Find the proper folder
############################################################################################################

for sub in subFolders:
    print (sub)
    print(sub.GetName())
    if sub.GetName() == 'PlaceHolders':
        print("found")
        #r.projectManager.OpenFolder(sub)
        mediaPool.SetCurrentFolder(sub)

#r.projectManager.GotoRootFolder()
#print(subFolders)
currentFolder = mediaPool.GetCurrentFolder()
print(currentFolder.GetName())

#clipFolder = mediaPool.OpenFolder('01 Assets')
#clipFolder = mediaPool.OpenFolder("01 Assets")

#clips = rootFolder.GetClipList()

############################################################################################################
# Get clips list
############################################################################################################

clips = currentFolder.GetClipList()
print(clips)

############################################################################################################
# Chose TimeLine , put time to 0 and delete everything
############################################################################################################

x = r.GetTimelinesByRegexp('12$')
for f in x:
    print(f"Opening '{f.GetName()}'")
    r.project.SetCurrentTimeline(f)
    tl = r.project.GetCurrentTimeline()
    print(tl.GetCurrentTimecode())
    tl.SetCurrentTimecode('00:00:00:00')
    print(tl.GetCurrentTimecode())
    #tl.AddTrack('video')
    tl.DeleteTrack('video',0)
    tl.DeleteTrack('video',1)
    tl.DeleteTrack('video',2)

y = r.GetTimelinesByRegexp('^PH')
for g in y:
    print(f"Timeline '{g.GetName()}'")
    r.project.SetCurrentTimeline(g)
    tl = r.project.GetCurrentTimeline()
    tl.SetCurrentTimecode('00:00:00:00')
    tl.AddTrack('video')
    tl.DeleteTrack('video',0)
    tl.DeleteTrack('video',1)
    tl.DeleteTrack('video',2)



# z = r.GetTimelinesByRegexp('^PH')
# for h in z:
#     print(f"Timeline '{h.GetName()}'")
#     r.project.SetCurrentTimeline(h)
#     tl = r.project.GetCurrentTimeline()
#     tl.SetCurrentTimecode('00:00:00:00')
#     tl.DeleteTrack('video',0)
#     tl.DeleteTrack('video',1)
#     tl.DeleteTrack('video',2)


############################################################################################################
# Chose TimeLine , put time to 0 and delete everything
############################################################################################################

z = r.GetTimelinesByRegexp('^PH')
for h in z:
    print(f"Opening '{h.GetName()}'")
    r.project.SetCurrentTimeline(h)
    tl = r.project.GetCurrentTimeline()
    print(tl.GetCurrentTimecode())
    tl.SetCurrentTimecode('00:00:00:00')
    print(tl.GetCurrentTimecode())
    for clip in clips:
        print(clip.GetName())
        #print(clip.GetClipProperty())
        properties = clip.GetClipProperty()
        print(properties['Usage'])
        if properties['Usage'] == '0':
            print("Clip found and appended")
            mediaPool.AppendToTimeline(clip)
            break
    #tl.AddTrack('video')


# for clip in clips:
#     print(clip.GetName())
#     #print(clip.GetClipProperty())
#     properties = clip.GetClipProperty()
#     print(properties['Usage'])
#     #if 
#     if clip.GetName() == "01.png":
#         print("Clip found and appended")
#         #mediaPool.AppendToTimeline(clip)