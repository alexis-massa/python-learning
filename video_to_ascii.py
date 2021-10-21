import os, glob, sys, shutil
from natsort import natsorted

import video_to_img
import img_to_ascii
import ascii_to_img
import img_to_video

# PARCOURIR DES FICHIERS DANS L'ORDRE
# DIR = './img'
# count_img = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

# filelist = glob.glob(os.path.join(DIR, '*.jpg'))
# for infile in natsorted(filelist): 
#   #do some fancy stuff
#   print(str(infile))

"""
  Convert video to frames - TODO
  Convert frames to ascii.txt - TODO
  Convert ascii.txt to ascii.jpg - TODO
  Convert ascii_img/*.jpg to out/video.avi  - TODO
"""

def main():

  # Check if file exists
  try:
    os.path.isfile(video_path)
  except:
    print(video_path, " isn't valid")

  # Empty all directories
  try:
    shutil.rmtree('./tmp')  
  except:
    print("tmp doesn't exist: skiping.")
  os.mkdir('./tmp')
  os.mkdir('./tmp/frames')
  os.mkdir('./tmp/ascii_img')
  os.mkdir('./tmp/in')
  os.mkdir('./tmp/out')
      


  # Extract frames from video
  video_to_img.video_to_img(video_path)



# Input video path
video_path = input("Enter path for the video to convert: ")
main()