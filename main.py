# environment:
import cv2
from pip import main
import os
import glob
import asyncio

# import files:
from loadAndSave_image import loadAndSave
from saveVideo import saveVideo
# from compare_images import ssimm
from yolo import yoloscore

########### Some changes on compare_images.py and yolo.py to use in the project ####################

# =========================yolo ===============================

# Return value : yolo score in string type
# Use the file need to call function: yoloscore()

# =========================compare_images.py===============================

# Return value : ssim,mae,mse score in string type
# Use this file need to call function: ssimm(pathA,pathB)
# pathA: cleaned-image file
# pathB: ground-truth file

# =========================How to use it===============================

# Function Description: 

# main():
# - Asynchronous function to load image
# - Clean&save image 
# - Read images into video
# - Apply yolo and compare_image function to get yolo score and matrics scores.
# - return yolo score ( if has correct yolo file)

# Variable describle:
# - tst_img_dir: corrupted images path
# - tst_dir: results images path
# - aim_img_dir: ground truth images path
# - data_path: path of corrupted images
# - files: read each corrupted images
# NOTE: path may need to change to suit where the path is.
# ===================================================================
async def main():
    
    tst_img_dir = './l2-ip-images/test/corrupted'
    tst_dir = './Results'
    aim_img_dir = './l2-ip-images/validation/ground-truth'
    
    data_path = os.path.join(tst_img_dir, '*png')
    files = glob.glob(data_path)
    
    # print("Loading images...")
    # # Clean&save images
    # await loadAndSave(files)
    # print("Images done!")
    # print("Loading videos...")
    # # when loadAndSave() finished, then run this function
    # # Read images into video
    await saveVideo(tst_dir + '/*png')
    print("Video done!")
    
    # when saveVideo() finished, then run next line
    # Apply yolo and compare_image function to get yolo score and matrics scores.
    
    ####### un-comment if has correct path ###################
    # avg_ssim, avg_mse, avg_mae = ssimm(tst_dir, aim_img_dir)
    #######un-comment if has correct yolo file ###################
    score = yoloscore()
    # get metrics scores and yolo score.

    # un-comment if has correct path
    # print("avg_ssim, avg_mse, avg_mae: " + avg_ssim, avg_mse, avg_mae)
    ###### un-comment if has correct yolo file ###################
    print(str(score))
    # return yolo score
    # return score

if __name__ == '__main__':
    asyncio.run(main())
