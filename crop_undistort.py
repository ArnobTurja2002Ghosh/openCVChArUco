import cv2
import numpy as np
import raw
import os
import time
import shutil
camera_matrix = np.load('camera_matrix.npy')
dist_coeffs = np.load('dist_coeffs.npy')


PATH_TO_YOUR_PAIRED = './pairedImages'
PATH_TO_YOUR_CROP = './UndistortAndCropThese'
image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_PAIRED) for name in files if name.endswith("_1.nef")]
image_files.sort()  # Ensure files are in order
currentlyReading={"image_file":None, "image_no": None, "newly_added": False}

def undistort():    
    for image_file in image_files:
        t1 = time.time()
        #print(cv2.imread(image_file).shape) # Load the image to ensure it exists

        image = raw.raw_to_npArray(image_file)
        undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
        print("UndistortAndCropThese/camShader"+image_file[image_file.index("\\")+1:])
        cv2.imwrite("UndistortAndCropThese/camShader"+image_file[image_file.index("\\")+1:-4]+".png", undistorted_image)
        t2 = time.time()
        print(f"Processed in {t2 - t1:.2f} seconds")

undistort()

image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files if "_" not in name]
image_files.sort()  # Ensure files are in order
for image_file in image_files:
    image=cv2.imread(image_file)
    image1=image[round(image.shape[0]/2-camera_matrix[1,2]) : , round(image.shape[1]/2-camera_matrix[0,2]) : ]
    print(image.shape, image1.shape)
    cv2.imwrite(image_file[:-4]+"_0.png", image1)

image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files if name.endswith("_1.png")]
image_files.sort()  # Ensure files are in order

for image_file in image_files: 
    print("Processing:", image_file)
    image = cv2.imread(image_file)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    # Define lower and uppper limits of what we call "brown"
    brown_lo=np.array([0,0,0])
    brown_hi=np.array([1, 1, 1])

    # Mask image to only select browns
    mask=cv2.inRange(hsv,brown_lo,brown_hi)

    # Change image to red where we found brown
    image[mask>0]=(255,255,255)

    cv2.imwrite(image_file[:-4]+"_white.png",image)
    print("Saved white image:", image_file[:-4]+"_white.png")

    image1=cv2.imread(image_file[:image_file.rindex("\\")]+"\\0_1.png")
    image1[mask>0]=(255,255,255)
    cv2.imwrite(image_file[:image_file.rindex("\\")]+"\\0_1_white.png",image1)
    image2=cv2.absdiff(image1, image)
    cv2.imwrite(image_file[:image_file.rindex("\\")]+"\\0_1_diff.png",image2)