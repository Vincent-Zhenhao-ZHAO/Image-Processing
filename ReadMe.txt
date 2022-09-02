########## Image Processing Code ###################
-   This file contains all code about cleaning the images by applying:
    -   Dewarping   ->  dewrap.py
    -   Noise Removal   ->  noise_reove.py
    -   Brightness and Contrast ->  brightness_and_contrast.py
-   main run file is main.py
-   tuning.py only use for tuning parameter process.
########## Requirment environment ###################
-   Python 3.7
-   opencv
########## How to use it ###########################
-   Open main.c 
-   follow the instruction in the code to input correct path as follows:
    - tst_img_dir: corrupted images path
    - tst_dir: results images path
    - aim_img_dir: ground truth images path
-   In command line, ensure in the same path as main.c
-   Then command line put: python main.py
######### code file explaintion #####################
-   main.py:    main function to Clean&save image, Read images into video, and 
    Apply yolo and compare_image function to get yolo score and matrics scores.
-   cleaning_image.py:  file helps to clean image by using three algorithms
-   loadAndSave_image.py:   load each image and clean the image by using cleaning_image.py
-   noise_remove.py:    contains three algorihtms to remove noise_reove:
    -   the medium filter,
    -   Non-local Means filter
    -   Bilateral Filter
-   dewrap.py:    contains an algorihtm to dewrap image:
-   brightness_and_contrast.py: contains three algorihtms to increase Brightness and Contrast:
    -   Histogram Equalisation
    -   Gamma Correction
    -   CLAHE
-   saveVideo.py:   import images into video
    -   Source code:
    -   https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv -- Rob answer
-   compare_image.py:   compare images between result and groud truth and return ssim,mae and mse scores.
    -   Note: this file has been changed into a function and return values
    -   To use it need to call function:    
        ssimm(pathA,pathB)
        pathA: cleaned-image file
        pathB: ground-truth file
    -   Author : Amir Atapour Abarghouei, amir.atapour-abarghouei@durham.ac.uk
    -   Copyright (c) 2021 Amir Atapour Abarghouei
    -   License : LGPL - http://www.gnu.org/licenses/lgpl.html

-   yolo.py:   Return yolo score. 
    -   Note: this file has been changed into a function and return values
    -   To use this file needs to call function:
        yoloscore()
        And need to change line 71 into video path
    -   Author : Amir Atapour Abarghouei, amir.atapour-abarghouei@durham.ac.uk
    -   Copyright (c) 2021 Amir Atapour Abarghouei
    -   License : LGPL - http://www.gnu.org/licenses/lgpl.html
- Result file: contains results images and video file called output_video.avi.

- output_video.avi: the result video, same as in result file. Just for easy to find.