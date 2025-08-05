import cv2
import numpy as np
import sys
sys.path.append('../')
import raw
import os
image_files1 = [os.path.join(path, name) for path, subdirs, files in os.walk("Discussion") for name in files]
image_files1.sort()  # Ensure files are in order
camera_matrix = np.load('../camera_matrix.npy')
PATH_TO_YOUR_PAIRED = '../chaarAdhyay'
PATH_TO_YOUR_CROP = './Discussion1'
image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_PAIRED) for name in files if name=="350.nef"]
image_files.sort()  # Ensure files are in order
def crop():
    for image_file1, image_file in zip(image_files1, image_files):
        image=cv2.imread(image_file1)
        image2=raw.raw_to_npArray(image_file)
        print(camera_matrix[1,2], image.shape[0]/2)
        if(image2.shape[0]/2 > camera_matrix[1,2]):
            image1=image[round(image.shape[0]/2-camera_matrix[1,2]) : , : ]
        elif(image2.shape[0]/2 < camera_matrix[1,2]):
            image1=image[ : image2.shape[0] , : ]
        if(image2.shape[1]/2 > camera_matrix[0,2]):
            image1=image1[ :, round(image1.shape[1]/2-camera_matrix[0,2]) : ]
        elif(image2.shape[1]/2 < camera_matrix[0,2]):
            image1=image1[ :, : image2.shape[1] ]
        print(image.shape, image1.shape, os.path.basename(PATH_TO_YOUR_PAIRED))
        print(os.path.join(PATH_TO_YOUR_CROP, os.path.dirname(image_file1)[os.path.dirname(image_file1).rindex("\\")+1:]+".png"))
        cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.dirname(image_file1)[os.path.dirname(image_file1).rindex("\\")+1:]+".png"), image1)

        # gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        # threshval, thresh = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        # print(threshval)
        # cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], "thresh_"+os.path.basename(image_file1)), thresh)

crop()