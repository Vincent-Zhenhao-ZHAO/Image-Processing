# environment
import cv2
import asyncio
# import files
from cleaning_image import image_cleaning
# =========================How to use it===============================
# - Use this file as functional file.
# - change path in cv2.imwrite into the path that you want to save the final image.
# - change -11 into the length of your name, including .png, for example: test001.png = -11
# ===================================================================
# loadAndSave(file,param) -> None:
# - Asynchronous function to read, clean and save image.
# ===================================================================
# Variable Description:
# - img: the size of the images
# - new_image: cleaned image
# NOTE: path may need to change to suit where the path is.
# ===================================================================

async def loadAndSave(file,param=None):
    for image in file:
        img = cv2.imread(image)
        new_image = image_cleaning(img,param)
        cv2.imwrite(
            './Results' + image[-11:], new_image)
    cv2.destroyAllWindows()
    