# environment:
import glob
import cv2

# =========================How to use it===============================
# - Use this file as functional file.
# - add param in each function if want to tune the parameter. eg: gamma(noise_remove,param)
# ===================================================================
# saveVideo(path) -> None:
# - Asynchronous function to import images into video
# ===================================================================
# Variable Description:
# - size: the size of the images
# - fourcc: video type(mp4 or avi etc)
# - out: final video
# ===================================================================
# Source code:
# - https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv -- Rob answer
# NOTE: path may need to change to suit where the path is.
# ===================================================================
async def saveVideo(path):
    size = (1024, 394)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out_video = cv2.VideoWriter('project.avi', fourcc, 3, size)
    for filename in sorted(glob.glob(path)):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img = cv2.resize(img, size)
        out_video.write(img)
        
    out_video.release()