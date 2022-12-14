# =========================How to use it===============================

# Return value : ssim,mae,mse score in string type
# Use this file need to call function: ssimm(pathA,pathB)
# pathA: cleaned-image file
# pathB: ground-truth file

# ===================================================================

# =========================Original=================================

# Example : compare images from two directories, the paths to which are
# specified on the command line - e.g. 
# python compare_images.py --dirA=path_to_dir_1 --dirB=path_to_dir_2
# python compare_images.py --dirA=../l2-ip-images/validation/ground-truth --dirB=../l2-ip-images/validation/corrupted

# Author : Amir Atapour Abarghouei, amir.atapour-abarghouei@durham.ac.uk

# Copyright (c) 2021 Amir Atapour Abarghouei

# License : LGPL - http://www.gnu.org/licenses/lgpl.html

# ===================================================================

import os
from skimage.metrics import structural_similarity as ssim
import argparse
import numpy as np
import cv2

# ===================================================================

# parse command line arguments for paths to the image directories

# ===================================================================

# function to calculate and output MSE and MAE between two images:

def compare_images(imageA, imageB):
	mse = np.sum((imageA - imageB) ** 2)
	mse /= float(imageA.shape[0] * imageA.shape[1])

	mae = np.mean(np.absolute((imageB - imageA)))

	return mse, mae

# ===================================================================
def ssimm(pathA,pathB):
	# lists to keep metrics:
	# parser = argparse.ArgumentParser(
    # description='Compare images from two directories')
    
	####### Orignal way to input file path ############
 
	# parser.add_argument(
	# 	"--dirA",
	# 	type=str,
	# 	help="specify path to directory A",
	# 	default='/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/validation/tests')

	# parser.add_argument(
	# 	"--dirB",
	# 	type=str,
	# 	help="specify path to directory B",
	# 	default='/Users/vincentzhao/Desktop/ImageCW/l2-ip-assignment/l2-ip-images/validation/ground-truth')

	# args = parser.parse_args()
 
	mses = []
	ssims = []
	maes = []

	# paths to directories:

	imageA_folder = pathA
	imageB_folder = pathB

	# looping through dir_A and reading all filenames:
	names = []

	for file in os.listdir(imageA_folder):
		
		names.append(file)

	# sort files by name and consider mac users:

	names.sort()
	if (".DS_Store" in names):
		names.remove(".DS_Store")

	# read images:

	for filename in names:
		
		imageA = cv2.imread(os.path.join(imageA_folder, filename), cv2.IMREAD_GRAYSCALE)
		imageB = cv2.imread(os.path.join(imageB_folder, filename), cv2.IMREAD_GRAYSCALE)

		if imageA is not None and imageB is not None:
				
			# convert images to floating point:
			
			imageA = imageA.astype("float") / 255
			imageB = imageB.astype("float") / 255
			
			# calculate MSE and MAE:
			mse, mae = compare_images(imageA, imageB)
			mses.append(mse)
			maes.append(mae)

			# calculate SSIM:
			ssims.append(ssim(imageA, imageB))

	# return the average of the three metrics:
 
	return str(sum(ssims)/len(ssims)), str(sum(mses)/len(mses)), str(sum(maes)/len(maes))


