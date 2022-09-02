# environment:
from cv2 import medianBlur
# import files
from noise_remove import fastNlMeansDenoising
from noise_remove import bilateralFilter
from noise_remove import medianBlur
from brightness_and_contrast import gamma
from brightness_and_contrast import his
from brightness_and_contrast import clahe
from dewrap import pta

# =========================How to use it===============================
# - Use this file as functional file.
# - add param in each function if want to tune the parameter. eg: gamma(noise_remove,param)
# ===================================================================
# image_cleaning(image,param=None) -> image:
# - function to clean image
# ===================================================================
# Variable Description:
# - dewrape: apply dewraping algorithm
# - noise_remove: apply noise_remove algorithm by using the result of dewrape
# - final: apply brightness and contrast algorihtm by using the result of noise_remove
# ===================================================================
def image_cleaning(image,param=None):
    dewrape = pta(image)
    noise_remove = fastNlMeansDenoising(dewrape)
    final = gamma(noise_remove)
    return final

