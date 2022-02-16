import os
import glob
import cv2
import numpy as np
from natsort import natsorted

DIR = './tmp/in/'
img_array=[]

def img_to_video():
    # Adds all frames with infos to an array
    for filename in glob.glob(os.path.join(DIR, "*.jpg")):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height) # output size (something wrong here)
        img_array.append(img)
    
    out = cv2.VideoWriter('./tmp/out/output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
    
    # array of img to video
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()