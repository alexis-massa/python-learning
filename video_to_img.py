import cv2

def getFrame(sec, count, vidcap):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./frames/"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

def video_to_img():
    video_path = input("Input the video to convert: ")
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