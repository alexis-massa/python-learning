import os
import glob
import cv2
import numpy as np
from natsort import natsorted

DIR = './img'
img_array=[]
    
def convert(size):
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def img_to_video():
    for filename in glob.glob(DIR, '*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (height, width)
        img_array.append(img)
        
        convert(size)