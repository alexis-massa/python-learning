import cv2

"""
    Extract frame
"""
def getFrame(sec, count, vidcap):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./tmp/frames/"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

"""
    Convert video to image
"""
def video_to_img(video_path):
    vidcap = cv2.VideoCapture(video_path)
    sec = 0
    frameRate = 0.1 # it will capture image in each 0.1 second (10FPS)
    count=1
    success = getFrame(sec, count, vidcap)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, count, vidcap)