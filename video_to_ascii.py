import os
import glob
from natsort import natsorted
import video_to_ascii
import img_to_ascii


DIR = './img'
count_img = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

# for img in os.listdir(DIR):
#     if os.path.isfile(os.path.join(DIR, img)):
#         print(img)

filelist = glob.glob(os.path.join(DIR, '*.jpg'))
for infile in natsorted(filelist): 
  #do some fancy stuff
  print(str(infile))