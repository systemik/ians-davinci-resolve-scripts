# Ian’s Resolve Scripts.

I started exploring the DaVinci Resolve API a little while back to see if there was an easy way to render a bunch of timelines at once … since I missed that from Premiere Pro. Turns out it IS possible, and a whole lot of other stuff besides.

# Requirements. 

These are scripts that I find super helpful and use nearly every day. I've tested them with Python 3 and Resolve 16, so if you're not using those then there's a good chance they won't work.

They're only tested on MacOS. I don't have Windows or Linux to try out.

Please note that there is NOT a lot of error checking. These are just little tools I've written for myself. They're not intended to be commercial grade software. Caveat, as they say, emptor.

# Installation.

Clone or download this repository and run them from the resulting folder. To run most everything you'll need [Python 3](https://www.python.org), [DaVinci Resolve 16](https://www.blackmagicdesign.com/products/davinciresolve).

To run `quickswitch.py` you'll also need [fzf](https://github.com/junegunn/fzf).

# The Scripts.

They're divided up into Renaming Things, Rendering Things, Opening Things, and Listing Things.

A couple of them use regular expressions. If you don't know what these are, they're very powerful and handy way to search text. There's [plenty of documentation](https://ryanstutorials.net/regular-expressions-tutorial/) out there.

## Renaming things

### renameTimelines.py

Rename Resolve timelines by specifying a regular expression.

**Example:**

```bash
> python3 renameTimelines.py '45$' 46
```
Rename every timeline that ends in `45`, by changing `45` to `46`. I use this for manually creating a new version of my timelines. This example would change `Bogus journey 45` to `Bogus journey 46`.

## Rendering things

### renderByRegexp.py

Pass this script a regular expression and this script will put each match into the render queue.

**Example:**

```bash
> python3 renderByRegexp.py --preset 'Quick MP4' --dest ~/work/renders --keep 'selects$'
```

This will render every timeline whose name ends in `selects`, using the preset `Quick MP4`, and set the destination folder to `~/work/renders`.

### renderBySuffix.py

This is kind of a convenience version of `renderByRegexp.py`, if you can't be bothered with regular expressions. Pass it a string and it will add each timeline with a matching *ending* to the render queue. 

For example, `renderBySuffix.py 24` will render a timeline named `example-timeline-24`, but not a timeline named `timeline-24-example`

**Example:**

```bash
> python3 renderBySuffix.py -p '720p MP4' -d ~/Desktop/ selects
```

This will render every timeline whose name ends in `selects`, using the preset named `720p MP4`, and setting the destination to `~/Desktop`.

## Opening things

### openLastFileInFolder.py

Open the most recent version of a project. Note that it only works on the filename.

Pass in the top level folder name, and it assumes that there are loads of files there named `Project 01`, `Project 02`, et cetera. Manual versioning.

This script lists them in alphabetical order and then opens the last one in the list. So … hopefully it works for you? 

**Example:** 

```bash
> python3 openLastFileInFolder.py MyDumbProject
```

Imagine your Resolve database had a folder at the top level called `MyDumbProject`. Inside you have a bunch of projects, named `DumbProject_01`, `DumbProject_02`, `DumbProject_03` etc. This will open `DumbProject_03`. In theory.

### openTimelinesMatchingRegexp.py

Pass it a regular expression (e.g. `final$` if you want to just match timelines that end in `final`) and this script will open each match in Resolve.

**Example:**

```bash
> python3 openTimelinesMatchingRegexp.py 'selects$'
```

This example will open every timeline whose name *ends* with the word `selects`. So it will open `futile banana selects` and `angry orangutan selects` but not `my selects 01`. 

### quickswitch.py

**NOTE:** this script requires [fzf, the Fuzzy Finder](https://github.com/junegunn/fzf).

If you have a project with a lot of timelines, this will let you sift through them quickly using the amazing fuzzy finding abilities of fzf. You select ONE timeline and `quickswitch.py` will open it for you.

## Listing things

These are all more or less the same, and they're about listing things, so here's a list:

- `listAllTimelines.py`
- `listCurrentTimecode.py`
- `listCurrentVideoItem.py`
- `listInfo.py`
- `listProjectsInCurrentFolder.py`
- `listRenderCodecs.py`
- `listRenderFormats.py`

These are very simple and do pretty much what you'd expect; they're just an easy way to query Resolve.

`listInfo.py` just combines several commands, "`GetProjectsInCurrentFolder`", "`GetRenderFormats`", and "`GetRenderPresets`". It's only notable because it prints the headings in a different colour, which was a small victory for me.
