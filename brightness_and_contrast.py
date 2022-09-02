# environement
import cv2
import numpy as np

# =========================How to use it===============================
# - Use this file as functional file.
# - Brigheness and contrast fucntions
# ===================================================================
# his(image) -> image:
# Histogram Equalisation
# ===================================================================
# gamma(image,gamma) -> image:
# Gamma Correction,
# ===================================================================
# clahe(image,clip_limit) -> image:
# CLAHE
# ===================================================================
def his(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(image)
    return dst

def gamma(image,gamma=0.8):
    image = ((np.power(image/255, gamma))*255).astype('uint8')
    return image

def clahe(image,clip_limit=2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clip_limit, tileGridSize=(2, 2))
    cl = clahe.apply(gray)
    return cl

