# environment:
import os
import glob
import asyncio
from matplotlib import pyplot as plt
# import files:
from loadAndSave_image import loadAndSave
from saveVideo import saveVideo

# from compare_images import ssimm
# from yolo import yoloscore

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
# - Use this file as main file.
# - change the path as quest below
# - change parameter range by changing min_ and max_
# - change what you want to tune in the orginal algorithm.
# Example: tune gamma -> go to cleaning_image -> gamma(noise_remove,param) -> change min_ and max_ -> Done
#  - This file require correct yolo file and compare image file
# ===================================================================
# processing(param=None) -> float:
# - Asynchronous function to load image
# - Clean&save image 
# - Read images into video
# - Apply yolo and compare_image function to get yolo score and matrics scores.
# - return yolo score and ssim score in float type

# Variable Description:
# - tst_img_dir: test corrupted images path
# - tst_dir: test results images path
# - img_dir: validation corrupted images path
# - fin_img_dir: validation results images path
# - aim_img_dir: ground truth images path
# - data_path: path of corrupted images
# - files: read each corrupted images
# NOTE: path may need to change to suit where the path is.
# ===================================================================
async def processing(param=None):
    tst_img_dir = '/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/test/corrupted'
    tst_dir = '/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/test/results'
    
    img_dir = '/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/validation/corrupted'
    fin_img_dir = '/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/validation/tests'
    aim_img_dir = '/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/validation/ground-truth'
    
    data_path = os.path.join(tst_img_dir, '*png')
    
    files = glob.glob(data_path)
    print("Loading images...")
    # Clean&save images
    await loadAndSave(files,param)
    print("Images done!")
    print("Loading videos...")
    # when loadAndSave() finished, then run this function
    # Read images into video
    await saveVideo(tst_dir + '/*png')
    print("Video done!")
    # when saveVideo() finished, then run next line
    # Apply yolo and compare_image function to get yolo score and matrics scores.
    ####### un-comment if has correct path ###################
    # avg_ssim, avg_mse, avg_mae = ssimm(fin_img_dir, aim_img_dir)
    ####### un-comment if has correct yolo file ###################
    # score = yoloscore()
    # get metrics scores and yolo score.
    ####### un-comment if has correct path ###################
    # print("avg_ssim, avg_mse, avg_mae: " + avg_ssim, avg_mse, avg_mae)
    # return yolo score and ssim score in float type.
    ####### un-comment if has correct yolo file ###################
    # return float(score),float(avg_ssim)

# ===================================================================
# optimiser(min_=None,max_=None) -> None:
# - Asynchronous function to tuning algorithm parameter
# - Every time only one parameter can be turned
# - The best parameter is base on highest yolo score
# - The result also will print ssim score as well in order to compare
# - Also will give the plot about ssim and yolo with parameter to have better picture
# ===================================================================

# Variable Description:
# - best_yolo_score: best yolo score
# - result: hashtable with paramter and ssim score, yolo score
# - yolo_score: yolo score list
# - ssim_scores: ssim score list
# - test_values: range of numbers need to test in algorihtm parameter

# ===================================================================

def optimiser(min_=None,max_=None):
    
    best_yolo_score = -1
    best_param = 0
    results = {}
    yolo_scores = []
    ssim_scores = []
    test_values = [i for i in range(min_, max_)]
    # tuning process
    for value in test_values:
        # get yolo and ssim score
        my_yolo_score,my_ssim_score = asyncio.run(processing(value))
        yolo_scores.append(my_yolo_score)
        ssim_scores.append(my_ssim_score)
        results[value] = (my_yolo_score,my_ssim_score)
        if my_yolo_score > best_yolo_score:

            best_yolo_score = my_yolo_score
            best_param = value
    # print the result list
    print(results)
    # print best parameter base on highest yolo score
    print(best_yolo_score, best_param)
    # draw plot base on parameter,yolo score, ssim score.
    drawplot(test_values,yolo_scores,ssim_scores)
    
# ===================================================================
# drawplot(param,yoloscore,ssim_score) -> None:
# - function to plot about ssim and yolo with parameter to have better picture
# ===================================================================

# Variable Description:
# - param: parameter list
# - yoloscore: yoloscore list
# - ssim_scores: ssim score list

# ===================================================================
def drawplot(param,yoloscore,ssim_score):
    fig, ax = plt.subplots(nrows=1,ncols=2)
    ax[0].title.set_text("yolo")
    ax[0].set_ylim([0.40, 0.90])
    ax[0].plot(param, yoloscore)
    
    ax[1].title.set_text("ssim")
    ax[1].set_ylim([0.20, 0.90])
    ax[1].plot(param, ssim_score)
    
    plt.show()
    
if __name__ == '__main__':
    optimiser()

