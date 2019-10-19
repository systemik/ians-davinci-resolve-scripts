#!/usr/bin/env python

"""
Example DaVinci Resolve script:
Display current media thumbnail from the color page using open cv plugin
You might need to install the opencv2 and numpy plugins where neccessary in order to run this script
"""

from python_get_resolve import GetResolve
import array
import base64
import cv2
import numpy as np

# Decode from base64 image string and return cv2 matrix image in BGR format for display
def readb64(base64_string, width, height):
    nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)
    nparr = nparr.reshape(int(height), int(width), 3)
    return cv2.cvtColor(nparr, cv2.COLOR_RGB2BGR)

if __name__ == "__main__":
    resolve = GetResolve()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()

    timeline = project.GetCurrentTimeline()
    currentMediaThumbnail = timeline.GetCurrentClipThumbnailImage()

    if (currentMediaThumbnail is None) or (len(currentMediaThumbnail) == 0):
        print("There is no current media thumbnail")

    width = currentMediaThumbnail["width"]
    height = currentMediaThumbnail["height"]
    format = currentMediaThumbnail["format"] # Currently we only have RBG 8 bit format

    print("Width of the thumbnail is " + str(width) + ", Height is " + str(height) + ", Format is " + str(format))

    imgstring = currentMediaThumbnail["data"]
    cvimg = readb64(imgstring, width, height)
    cv2.imshow("Current Media Thumbnail", cvimg)
    cv2.waitKey()
