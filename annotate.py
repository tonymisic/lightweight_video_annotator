import cv2, os
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

# helpers
def get_frames(video_file):
    cap = cv2.VideoCapture(video_file)
    frames = []
    success, image = cap.read()
    while success:
        frames.append(image)
        success, image = cap.read()
    if len(frames) <= 1:
        print("Error loading file!")
        return frames
    return frames

def get_files(folder):
    result = []
    for f in os.listdir(folder):
        result.append(folder + "/" + f)
    return result

# globals
current_frame, current_video = 0, 0
save = open("save", 'r')
current_video = int(save.readline())
save.close()
files = get_files('./videos') #change this
label = "Baseball Pitch" # change this
clip = get_frames(files[current_video])
# START
root = tk.Tk()
# frames
top = tk.Frame(root)
bottom = tk.Frame(root)
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# load first image
img = ImageTk.PhotoImage(image=Image.fromarray(clip[current_frame]))
canvas = tk.Canvas(root,width=700,height=700)
canvas.pack(in_=top, side=tk.LEFT, fill=tk.BOTH, expand=True)
image_on_canvas = canvas.create_image(200,20, anchor="n", image=img)
# texts
text = tk.Label(root, width=30, height=1, text="")
text.pack(in_=top, side=tk.LEFT, fill=tk.BOTH, expand=True)
text.configure(text="Current Frame: " + str(current_frame) + "/" + str(len(clip)))
counter_text = tk.Label(root, width=30, height=1, text="")
counter_text.pack(in_=top, side=tk.LEFT, fill=tk.BOTH, expand=True)
counter_text.configure(text="Current Video: " + str(current_video + 1) + "/" + str(len(files)))

def set_anno(obj):
    global current_frame
    obj.configure(text=current_frame)

def create_button_set(anno):
    subtitle = tk.Label(root, width=30, height=1, text=anno)
    subtitle.pack(in_=top, side=tk.TOP, fill=tk.BOTH, expand=True)
    frame = tk.Label(root, width=30, height=1, text=str(0))
    frame.pack(in_=top, side=tk.TOP, fill=tk.BOTH, expand=True)
    button = tk.Button(root, text='Set',command=lambda *args: set_anno(frame))
    button.pack(in_=top, side=tk.TOP)
    return frame
# annotation information
fil = open('annotations.txt', 'r') # this needs to be downloaded
annotations = []
for line in fil.readlines():
    annotations = line.split(',')
key_frames = []
for i, anno in enumerate(annotations, 0):
    f = create_button_set(anno)
    key_frames.append(f)
fil.close()
def change_text():
    global text
    global counter_text
    global current_frame
    global current_video
    global clip
    text.configure(text="Current Frame: " + str(current_frame) + "/" + str(len(clip)))
    counter_text.configure(text="Current Video: " + str(current_video + 1) + "/" + str(len(files)))

def changeFrame(change):
    global current_frame
    global img
    global clip
    global canvas
    global image_on_canvas
    if current_frame + change < len(clip) and current_frame + change >= 0:
        current_frame += change
    img = ImageTk.PhotoImage(image=Image.fromarray(clip[current_frame]))
    canvas.itemconfig(image_on_canvas, anchor="n", image=img)
    change_text()

def changeFile():
    global current_frame
    current_frame = 0
    global current_video
    global files
    global clip
    global key_frames
    global label
    f = open("video_annos.txt", 'a')
    temp = ','.join([ files[current_video].split('/')[2], label, ','.join([str(key["text"]) for key in key_frames])]) + '\n'
    f.write(temp)
    f.close()
    for key in key_frames:
        key.configure(text=0)
    if current_video + 1 < len(files):
        current_video += 1
        save = open("save", 'w')
        save.write(str(current_video))
        save.close()
    clip = get_frames(files[current_video])
    changeFrame(0)
    change_text()
    
    

tk.Button(root, text='-100',command=lambda *args: changeFrame(-100)).pack(in_=bottom, side=tk.LEFT)
tk.Button(root, text='-10',command=lambda *args: changeFrame(-10)).pack(in_=bottom, side=tk.LEFT)
tk.Button(root, text='-1',command=lambda *args: changeFrame(-1)).pack(in_=bottom, side=tk.LEFT)
tk.Button(root, text='+1',command=lambda *args: changeFrame(1)).pack(in_=bottom, side=tk.LEFT)
tk.Button(root, text='+10',command=lambda *args: changeFrame(10)).pack(in_=bottom, side=tk.LEFT)
tk.Button(root, text='+100',command=lambda *args: changeFrame(100)).pack(in_=bottom, side=tk.LEFT)

tk.Button(root, text='Finish',command=lambda *args: changeFile()).pack(in_=bottom, side=tk.LEFT)
# END
root.mainloop()
