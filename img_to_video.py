import os
import glob
import cv2
import numpy as np
from natsort import natsorted
import re

DIR = './tmp/in/'
img_array=[]


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def img_to_video():
    # Adds all frames with infos to an array
    for filename in sorted(glob.glob(os.path.join(DIR, "*.jpg")), key=numericalSort):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height) # output size (something wrong here)
        img_array.append(img)
    
    out = cv2.VideoWriter('./tmp/out/output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
    
    # array of img to video
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()