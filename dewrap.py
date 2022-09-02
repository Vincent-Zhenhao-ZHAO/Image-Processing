# environment
import cv2
import numpy as np

# =========================How to use it===============================
# - Use this file as functional file.
# - dewraping by using warp perspective function
# ===================================================================
# pta(image) -> image:
# - function to dewraping image.
# ===================================================================
# Variable Description:
# - pts1: four points of the image bourndry
# - pts2: four points of the whole image coundry
# ===================================================================
def pta(image):
    pts1 = np.float32([[20, 20], [949, 9], [19, 387], [961, 373]])
    pts2 = np.float32([[0, 0], [1024, 0], [0, 394], [1024, 394]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(image, matrix, (1024, 394))
    return result