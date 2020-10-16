# Lightweight Video Annotator for Labelling Key Frames of Actions
Made with python and associated libraries
## Installation
 - Download zip from this repository
 - Unzip into parent directory of folder containing videos
 - Format should look something like this:
 ```
  .
  +-- annotate.py
  +-- annotations.txt
  +-- save
  +-- video_annos.txt
  +-- videos
  |   +-- example1.mp4
  |   +-- example2.mp4
 ```

## Setup
 - **annotate.py** change the following variables:
      ```
      files = get_files('./videos') # change the string to the name of your video folder
      label = "Baseball Pitch" # change to what the current label of the videos is
      ```
 - **annotations.txt** is one line of key event names, delimited by commas and should be changed to the key events you need. It can handle 1-8 key events.
 - **save** is the file number you are currently left at, as you work on images it will save your progress and let you continue if you close the program.
 - **video_annos.txt** the output file, formatted: filename,label,keyframe,keyframe,keyframe,keyframe 
## Compiling and Running
```
$ python annotate.py
```
If you are missing any dependencies:
```
$ pip install <library>
```
## Using the GUI
