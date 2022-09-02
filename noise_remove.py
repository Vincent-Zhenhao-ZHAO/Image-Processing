# environment
import cv2

# =========================How to use it===============================
# - Use this file as functional file.
# - noise_removal fucntions
# ===================================================================
# medianBlur(image,neighbourhood=5) -> image:
# the medium filter,
# ===================================================================
# fastNlMeansDenoising(image,h=25) -> image:
# Non-local Means filter
# ===================================================================
# bilateralFilter(image,sigma=11): -> image:
# Bilateral Filter
# ===================================================================
def medianBlur(image, neighbourhood=5):
    
    median_img = cv2.medianBlur(image, neighbourhood)
    return median_img

def fastNlMeansDenoising(image,h=25):
    
    dsc = cv2.fastNlMeansDenoising(image, None, 8, 5, h)
    return dsc

def bilateralFilter(image,sigma=11):
    
    bf = cv2.bilateralFilter(image,5,sigma,sigma,None)
    return bf
