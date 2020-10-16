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
      label = "baseball_pitch" # change to what the current label of the videos is
      files = get_files('./videos', label) # change the string to the name of your video folder
      ```
 - **annotations.txt** is one line of key event names, delimited by commas, each line being an action
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
 - Traversing frames: [Link to Video](https://drive.google.com/file/d/1jDdKD4jmL_n9R5qhz76NqnUGDOtpSjf8/view?usp=sharing)
 - Set current frame as key frame and saving: [Link to Video](https://drive.google.com/file/d/1VG-d4zTPRwDVnvMfLeIh19QJJyA4d-hy/view?usp=sharing)
