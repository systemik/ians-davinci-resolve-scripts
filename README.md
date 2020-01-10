# Ian’s Resolve Scripts

## Rendering things

### renderByRegexp.py

Pass this script a regular expression (e.g. `24$` to render every timeline
that ends in `24`) and this script will put each match into the render queue.

**Example:**

```bash
> python3 renderByRegexp.py --preset 'Quick MP4' --dest ~/work/renders --keep 'selects$'
```

This will render every timeline whose name ends in "selects", using the preset "Quick MP4", and set the destination folder to "~/work/renders".

### renderBySuffix.py

Kind of convenience version of `renderByRegexp.py`. Pass it a string and it will add each timeline with a matching *ending* to the render queue. E.g. `renderBySuffix.py 24` will render

`example-timeline-24`

but not

`timeline-24-example`

**Example:**

```bash
> python3 renderBySuffix.py -p '720p MP4' -d ~/Desktop/ selects
```

This will render every timeline whose name ends in "selects", using the preset named "720p MP4", and setting the destination to "~/Desktop".

## Opening things

### openLastFileInFolder.py

Open the most recent version of a project. Note that it only works on the filename.

Pass in the "top level" folder name, and it assumes that there are loads of 
files there named "Project 01" "Project 02" et cetera. Manual versioning.

This script lists them in alphabetical order and then opens the last one in the list. So … hopefully it works for you? 

### openTimelinesMatchingRegexp.py

Pass it a regular expression (e.g. "24$" if you want to just match timelines that end in "24") and this script will open each match in Resolve.

### quickswitch.py

**NOTE:** this script requires [fzf, the Fuzzy Finder](https://github.com/junegunn/fzf).

If you have a project with a lot of timelines, this will let you sift through them quickly using the amazing fuzzy finding abilities of fzf. You select ONE timeline and `quickswitch.py` will open it for you.

## Listing things

- `listAllTimelines.py`
- `listCurrentTimecode.py`
- `listCurrentVideoItem.py`
- `listInfo.py`
- `listProjectsInCurrentFolder.py`
- `listRenderCodecs.py`
- `listRenderFormats.py`

These are very simple and do pretty much what you'd expect; they're just an easy way to query Resolve.

`listInfo.py` just combines several commands, "`GetProjectsInCurrentFolder`", "`GetRenderFormats`", and "`GetRenderPresets`". It's only notable because it prints the headings in a different colour, which was a small victory for me.
