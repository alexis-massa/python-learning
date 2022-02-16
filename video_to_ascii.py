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
  Convert video to frames - DONE
  Convert frames to ascii.txt - DONE
  Convert ascii.txt to ascii.jpg - DONE
  Convert ascii_frames/*.jpg to out/video.avi  - TODO
"""

"""
  Checks if video exists
  Recreate tmp directories
"""
def check(video_path):
    # Check if file exists
  try:
    os.path.isfile(video_path)
  except:
    print(video_path, " isn't valid")
    return 0

  # Empty all directories
  try:
    shutil.rmtree('./tmp')  
  except:
    print("tmp doesn't exist: skiping.")
  os.mkdir('./tmp')
  os.mkdir('./tmp/frames')
  os.mkdir('./tmp/ascii_frames')
  os.mkdir('./tmp/in')
  os.mkdir('./tmp/out')
  return 1


def main():
  # Input video path
  video_path = 'C:/LocalRepository/python-learning/video/video.mp4'
  # video_path = input("Enter path for the video to convert: ")

  # Perform checks
  if(check(video_path)==0):
    exit
  
  # Extract frames from video
  video_to_img.video_to_img(video_path)
  print('video to frames : OK')

  # foreach image : convert to ascii
  for ascii_filename in os.listdir('./tmp/frames'):
    ascii_filepath = os.path.join('./tmp/frames', ascii_filename)
    # checking if it is a file
    if os.path.isfile(ascii_filepath):
      img_to_ascii.img_to_ascii(ascii_filepath, os.path.splitext(ascii_filename)[0], 480)
  print('frames to ascii_frames : OK')

  # foreach ascii : convert to img 
  for txt_filename in os.listdir('./tmp/ascii_frames'):
    txt_filepath = os.path.join('./tmp/ascii_frames', txt_filename)
    # checking if it is a file
    if os.path.isfile(txt_filepath):
      ascii_to_img.ascii_to_img(txt_filepath)
  print('ascii_frames to img input : OK')
  img_to_video.img_to_video()
  print('img to video : OK')
  print('---------------------------- DONE ----------------------------')

main()